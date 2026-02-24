import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, to_date, when, regexp_replace, expr
from pyspark.sql.types import IntegerType, DateType
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
input_path = "s3://driven-data-bucket-again19/raw_data/"
dynamic_frame = glueContext.create_dynamic_frame.from_options(
 connection_type="s3",
 connection_options={"paths": [input_path]},
 format="csv",
 format_options={"withHeader": True}
)
df = dynamic_frame.toDF()
df = df.na.fill({"email": "unknown@example.com", "phone": "000-000-0000"})
df = df.withColumn("birth_date", col("birth_date").cast(DateType()))
df = df.withColumn("session_duration", col("session_duration").cast(IntegerType()))
df = df.dropDuplicates(subset=["unique_id"])
df_filtered = df.filter((df["session_duration"] > 30) & (to_date(df["accessed_at"]) > "2024-01-01"))
df_filtered = df_filtered.withColumn("total_bandwidth", col("download_speed") + col("upload_speed"))
df_filtered = df_filtered.withColumn("activity_level", when(col("session_duration") > 120, "active")
                                    .when(col("session_duration").between(30, 120), "moderate")
                                    .otherwise("less_active"))
df_filtered = df_filtered.withColumn("masked_email", regexp_replace("email", "(\\w{3})\\w+@(\\w+)", "$1***@$2"))
df_grouped = df_filtered.groupBy("person_name").agg({"session_duration": "avg", "consumed_traffic": "sum"})
filtered_dynamic_frame = DynamicFrame.fromDF(df_filtered, glueContext, "filtered_dynamic_frame")
grouped_dynamic_frame = DynamicFrame.fromDF(df_grouped, glueContext, "grouped_dynamic_frame")
output_path = "s3://driven-data-bucket-again19/transformed_data/"
glueContext.write_dynamic_frame.from_options(
 frame=filtered_dynamic_frame,
 connection_type="s3",
 connection_options={"path": output_path + "filtered/"},
 format="csv",
 format_options={"header": True}
)
glueContext.write_dynamic_frame.from_options(
 frame=grouped_dynamic_frame,
 connection_type="s3",
 connection_options={"path": output_path + "grouped/"},
 format="csv",
 format_options={"header": True}
)
job.commit()                                    
            