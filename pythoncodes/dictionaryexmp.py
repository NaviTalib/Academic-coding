dicn={"talib":1,"deppak":2,"akash":3,"ajeet":4,"chandan":{"aman":11,"rahul":12}}
print(dicn)
print(dicn["talib"])
dicn["ankit"]=13
del dicn["akash"] #for delete value form dictionary
dicn1=dicn
dicn1.update({"ajeet":6}) #for update value
print(dicn1)
print(dicn1.keys())