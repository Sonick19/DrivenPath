with source as (
    select * from read_csv_auto('data/raw_payments.csv')
)

select * from source