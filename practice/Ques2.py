import pandas as pd
s=pd.Series(['2023-01-01','not a data','2024-05-10'])
dt_s=pd.to_datetime(s,errors='coerce')
valid_date=dt_s.dropna()
print(valid_date)