import pandas as pd
import numpy as np
data={"days":[1,2,3,4,5,6,7,8,9,10],
     "steps":[3456,6789,4567,6547,8907,5678,6789,4567,8967,8765]}
dp=pd.DataFrame(data)
dp["+1000 steps"]=dp["steps"]+1000
fi=dp[dp["+1000 steps"]>7000]["days"]
print("DataFrame:\n",dp)
print("\ndays on which steps were > 7000:\n",fi)