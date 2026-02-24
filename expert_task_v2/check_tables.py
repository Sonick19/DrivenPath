import duckdb

con = duckdb.connect('result.duckdb')
df = con.execute("SELECT * FROM main.customers LIMIT 15;").fetchdf()
print(df)