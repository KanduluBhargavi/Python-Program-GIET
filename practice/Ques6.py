import pandas as pd
data={'A':[1,2,3],
      'b':[4,5],
      "c":[6,7,8,9]}
df=pd.DataFrame(dict([(k,pd.Series(v)) for k,v in data.items()]))
df=df.where(pd.notnull(df),None)
print(df)
