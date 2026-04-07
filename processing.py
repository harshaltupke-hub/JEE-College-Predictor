import  pandas as pd
import numpy as np

from user_ipop import user_input
from user_ipop import home_state

if user_input[1]=="JEE Mains":
    df=pd.read_csv("Mainlogic.csv")
else:
    df=pd.read_csv("ADVlogic.csv")
#user_input = user_input+[rank, exam, gender, state, category, program, college]

Rank=user_input[0]

filtered=df[
            (df["Institute"]==user_input[6])&
            (df["Academic Program Name"]==user_input[5])&
            (df["Seat Type"]==user_input[4])&
            (df["Gender"]==user_input[3])]
lower=0
upper=0
if not filtered.empty:
    lower=filtered['lower_limit'].min()
    upper=filtered['upper_limit'].max()
else:
    print("NO matching record found")

f1 = len(df[df["Institute"] == user_input[6]])
f2 = len(f1[f1["Academic Program Name"] == user_input[5]])
f3 = len(f2[f2["Seat Type"] == user_input[4]])
f4 = len(f3[f3["Gender"] == user_input[3]])

if f2==0:
    print(f"{user_input[5]} is not available in {user_input[6]}")
elif f3==0:
    print(f"{user_input[4]} is not available in {user_input[6]}")
elif f3==0:
    print(f"{user_input[3]} is not available in {user_input[6]}")
else:
    pass