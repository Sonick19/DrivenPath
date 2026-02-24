
  
  create view "result"."main_staging"."staging_customers__dbt_tmp" as (
    with source as (
    select * from "result"."main_raw"."raw_customers"

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed
  );
