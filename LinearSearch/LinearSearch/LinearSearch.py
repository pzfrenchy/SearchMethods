list = [5,3,8,6,4,1,2]

def Search(l, t):
    found = False
    length = len(l)
    for i in l:
        if i == t:
            found = True
    return found

term = int(input("Please enter a search term: "))
result = Search(list, term)
if result == True:
    print("term found")
elif result == False:
    print("term not found")