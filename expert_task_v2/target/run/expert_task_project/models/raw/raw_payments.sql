
  
    
    

    create  table
      "result"."main_raw"."raw_payments__dbt_tmp"
  
    as (
      with source as (
    select * from read_csv_auto('data/raw_payments.csv')
)

select * from source
    );
  
  