#to merge two dataframes 
import pandas as pd
df1=pd.DataFrame({'id':[1,2,3],'name':['selena','anna','caeso'],
                  })
df2=pd.DataFrame({'id':[2,3],'name':['anna','caeso']})
merged_df=pd.merge(df1,df2,on='id',how='right')
print(merged_df)