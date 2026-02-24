
  
    
    

    create  table
      "result"."main_raw"."raw_customers__dbt_tmp"
  
    as (
      with source as (
    select * from read_csv_auto('data/raw_customers.csv')
)

select * from source
    );
  
  