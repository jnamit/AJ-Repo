import pyarrow.parquet as pq
import pandas as pd

table2 = pq.read_table('example.parquet')
print(table2.to_pandas())
table2.to_pandas().to_csv("example.csv")
