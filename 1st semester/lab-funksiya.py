import random
a = [random.randint(1, 100) for x in range(10)]
print(a)
b = [1, 2, 3, 4, 5]

myList = ["""

"""]



for x in myList:
    myList2 = x.split("\n")
    for k in myList2:
        if k != "":
            print("\n", k)
            if bool("=" in k or "import" in k) == False:
                eval(k) 