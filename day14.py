'''Mapping --> Dictionaries -->key value pairs used to store related data -- > JSON,APIS,database records

dic() --> data={}

details={}
print(type(details))

details={"Id":"CGH4022","name":"manasa",
         "gender":"f","age":20,
         "batch":"da23","place":"hyd"
         }
print(details)
print(len(details))


#access the data from dictionary

details[0] #key error

print(details.keys())
print(details["Id"],details["name"])
details['marks']=[]
print(details)
details["marks"].append(20)
print(details)

details['marks'].extend([15,20,25,30,35])
print(details)

#create a key-value pair of practice session
details={}
details["ps"]=("tuesday","thusrday","saturday")
print(details.keys())
print(details['marks'][2])
print(details['ps'][1])
print("wednesday" in details)
print("mi" in details)

details={"Id":"CGH4022","name":"manasa",
         "gender":"f","age":20,
         "batch":"da23","place":"hyd"}
print(details)
for i in details.key():
    print(f"key = {i}")
    print(f"value = {details(i)}

details={"Id":"CGH4022","name":"manasa",
         "gender":"f","age":20,
         "batch":"da23","place":"hyd"}
details["ps:"]=("tuesday","thusrday","saturday")

for i in details.values():
    print(i)
for i in details.items():
    print(i)
    
for key,value in details.items():

#update --> updating the dictionary with key-value pairs
details .update({"marks":[],
                "ps":("tuesday","thursday","saturday")})
'''
details={"Id":"CGH4022","name":"manasa",
         "gender":"f","age":20,
         "batch":"da23","place":"hyd"}
print(details.key())
print(details.get("name"))
print(details.get("branch"))

details.setdefault("branch")
print(details)
details["branch"]="cse"
print(details)

print(details.pop("branch"))
print(details.keys())

print(details.popitem())
print(details.keys())

















































print(details=setdefault("name"))




















    
