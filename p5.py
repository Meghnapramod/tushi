import pandas as pd
p={'course':["py","jv","dbms","mma","s&a"],
   'fee':[300,600,21,350,67],
   'complexity':[100,56,32,10,57]}
d=pd.DataFrame(p)
print(d)
print("\n",d.pivot(columns='course',values='complexity'))
print("\n",d.melt())
