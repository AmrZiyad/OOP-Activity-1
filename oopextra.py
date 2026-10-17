class scooty:
    def __init__(self,name,appearence):
        self.name = name
        self.appearence = appearence

class car:
    def __init__(self,name,appearence):
        self.name = name
        self.appearence = appearence

ob = scooty("activa","blue")
print(ob.name,ob.appearence)

ob1 = car("swift","gray")
print(ob1.name,ob1.appearence)

print("Thank you!")