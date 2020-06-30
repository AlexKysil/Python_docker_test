for counter in range (1,4):
    print("user" + str(counter))

dict= {}

dic= {"email": "smb", "password": "ggwp"}
bbg= {"connection": "obj"}

dict.update({"user1":{"credits": dic, "obj": bbg}})
print(dict)
print(dict['user1']['credits']['email'])
print(dict['user1']['credits']['password'])
print(dict['user1']['obj']['connection'])

print("hello")
print("again")


print("one more commit")
