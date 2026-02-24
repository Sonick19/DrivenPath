
  
    
    

    create  table
      "result"."main_raw"."raw_orders__dbt_tmp"
  
    as (
      with source as (
    select * from read_csv_auto('data/raw_orders.csv')
)

select * from source
    );
  
  