import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
student=pd.DataFrame({'school_code':['s001','s002','s003','s001','s002','s004'],'A':[1,2,3,3,8,6],
      'b':[4,5,7,8,8,4],
      'c':[6,7,8,9,9,3]})
result=student.groupby(['school_code'])
for name,group in result:
    print(name,group)
