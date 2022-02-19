def two_fer(name=""):
    if name:
        return("One for ",name ," one for me")
    else:
        return("One for you ,one for me")
x=input("enter name")
print(two_fer(x))


