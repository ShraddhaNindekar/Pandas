import pandas as pd
student={"Name":["Neha","Prachi","Leena","Riya","Soniya","Sakshi","Heena"],
"Age":[23,34,24,22,28,30,29],
"City":["Nagpur","Nagpur","Mumbai","Pune","Delhi","Mumbai","Pune"],
"Marks":[56,78,96,85,82,76,67]}
print(student)
df=pd.DataFrame(student)
print(df)
print(df.head(1))
print(df.head(2))
print(df.head())
print(df.tail(1))
print(df.tail(2))
print(df.shape)
print(df.dtypes)
print(df.columns)
print(df["Name"])
print(df["City"])
print(df["Age"])
print(df["Marks"])
print(df[["Name","Marks"]])
print(df[df["Marks"]>=70])
print(df[df["City"]=="Nagpur"])
print(df[df["City"]=="Mumbai"])
print(df[df["Age"]<=25]) 


