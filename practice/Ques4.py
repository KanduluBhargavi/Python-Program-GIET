import pandas as pd
s=pd.Series(['apple','banana','apple','orange'])
cat_s=s.astype('category')
print(cat_s.cat.codes)
print(cat_s)

p=pd.Series(['lion','cat','dog','tiger','monkey','dog','cat'])
anim_s=p.astype('category')
print(anim_s)
print(anim_s.cat.codes)