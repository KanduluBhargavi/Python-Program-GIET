import pandas as pd
s=pd.Series(['10','20',"abc","40"])
numeric_s=pd.to_numeric(s,errors="coerce")
print(numeric_s)

"""errors="coerce" if the conversion is possible -> converts normally . and if the conversion is not possible -> replaces with NaN"""

