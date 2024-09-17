import pandas as pd

data ={
"Name" :["shipra","vidhi","nikita"],
"Age" :[20,22,19],
"City":["ghaziabad","delhi","noida"]

}
filepath=r"C:\Users\Lenovo\Desktop\pythonws\sample1.xlsx"
df= pd.DataFrame(data)
df.to_excel(filepath ) 
df = pd.read_excel(filepath)
print(df.head())