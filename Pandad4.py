# multiple concepts in one dataset 
import pandas as pd
stu_data={"Name":["Anushka","Gauri","Shital","Heena","Kasak","Shruti","Siya","Riya","Akansha"],
"City":["Nagpur","Nagpur","Pune","Mumbai","Mumbai","Pune","Haidrabad","Hidrabad","Delhi"],
"Python_Marks":[80,67,98,49,70,89,79,46,58],
"Sql_Marks":[43,56,32,65,34,78,65,22,90],
"Attendance":[90,98,95,89,85,88,94,78,80],
"Age":[23,30,22,24,20,29,26,26,27]}
df=pd.DataFrame(stu_data)
print(df)
print("==================")
print(df.head())
print("==================")
print(df.tail())
print("==================")
print(df.shape)
print("==================")
print(df.head(2))
print("==================")
print(df.dtypes)
print("==================")
print(df["Name"])
print("==================")
print(df["Age"])
print("==================")
print(df[["Name","Age","City"]])
print("==================")
print(df[["Python_Marks","Sql_Marks"]])
# Filtering data 
print(df[df["Python_Marks"]>=80])
print(df[df["City"]=="Pune"])
print(df[df["City"]=="Nagpur"])
print("==================") 
print(df.tail(3))
print(df.shape)
print(df.dtypes)
print(df.columns)
print(df[df["Python_Marks"]>80])
print(df[df["Sql_Marks"]>=85])
print(df[df["City"]=="Nagpur"])
print(df[df["City"]=="Pune"])
print(df[df["Attendance"]>90])
print(df[df["Python_Marks"]<70])
print(df[(df["City"]=="Nagpur")& (df["Python_Marks"]>=80)])
print(df[(df["City"]=="Pune")&(df["Attendance"]>=90)])
# print(df[(df["Python_Marks"] >= 80) & (df["Sql_Marks"] >= 80)])
# print(df[(df["Attendance"]>=85)& (df["Sql_Marks"]>=80)])
# print(df[(df["City"]=="Mumbai")& (df["Python_Marks"]>=75)])

# Nagpur ke students jinke Python marks 80+ hain.
# print(df[(df["City"]=="Nagpur")& (df["Python_marks"]>=80)])
# # Pune ke students jinki attendance 90+ hai.
# Students jinke Python marks 80+ AND SQL marks 80+ hain.
# Students jinki attendance 85+ AND Python marks 80+ hain.
# Mumbai ke students jinke Python marks 75+ hain.
