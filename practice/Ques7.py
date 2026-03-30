import pandas as pd
data={'a':[1,2,3],
      'b':[4,5,6]}
df=pd.transpose(data)
df_t=df.T
print("original ",df)
print(df_t)