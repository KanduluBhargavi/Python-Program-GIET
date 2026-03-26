import pandas as pd
data={'name':["alice","bob","charlie"],
      "age":[25,30,35],
      "city":["newyork","sanfransico","losangeles"]}
pd1=pd.DataFrame(data)
print(pd1["age"])