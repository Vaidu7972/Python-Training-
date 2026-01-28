"""
DICTIONARY = {"Key" : "value"} pairs (unorder, mutable, don't duplicate keys.)
"""
dic={
    "key" : "value",                #we can store str,int,boolean,float,list.set..
    "name" : "vaidehi",
    "age" : 20,
    "is adult" : True,
    "Marks" : 98.0,
    "subject": ["Python","Java"],
    "hobby": ("reading","coding"),
    1 : "one",
    2 : 400,                        #we can make int as key
    }
print(dic)
print(type(dic))
print(type(dic),len(dic))
print(type(dic),"\n")

#  ACCESSING DICTIONARY

print(dic["name"])                        #used to access value of key
print(dic[1],"\n")

#  ADDING ITEMS IN DICTIONARY

dic["Surname"]="Doke"
print(dic,"\n")

#  REPLACING OR CHANGE

dic["name"] =  "Vaidehi Doke"
print(dic,"\n")

dic[2] = 500
print(dic,"\n")

#  NULL DICTIONARY
null_dic={}
print(null_dic)
print(type(null_dic),len(null_dic))

null_dic["name"]="prateek"
print(null_dic)

#  NESTED DICTIONARY

stu={
    "name" : "vaidehi",
    "age": 20,
    "marks": {
        "python": 98,
        "java": 95
    }
}
print(stu,"\n")

#  DICTIONARY METHODS

print(stu.keys())                    #keys = return all keys 
print(stu.values())                  #Values = returns values 
print(len(stu))                      #length of key

print(stu.items())                   #items = return all key value in form of list
print(stu.get("name"))               #get = return value of specified key

stu.update({"city" : "hi"})          #update = update or add new 
print(stu)

stu.update({"name" : "as"})
print(stu,"\n")


