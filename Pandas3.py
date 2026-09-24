import pandas as pd;
Employees={"Emp_Name":["Kajal","Shreya","Sakshi","Akansha","Ruchika","Kiran"],
"Department":["Data Analyst","Python Developer","Web developer","Business Analyst","Sales Executive","Digital Marketing"],
"Experience":[1,3,6,7,8,2],
"Salary":[40000,80000,70000,65000,72000,60000]}
df=pd.DataFrame(Employees)
print(df)
#  first 5 employee
print(df.head())
# Dataset shape
print(df.shape)
# Column names
print(df.columns)
# Data types
print(df.dtypes)
# Employees with experience greater than 2 years
print(df[df["Experience"]>2])
# Employees with salary greater than 50000
print(df[df["Salary"]>50000]) 
