with source as (
    select * from read_csv_auto('data/raw_orders.csv')
)

select * from source