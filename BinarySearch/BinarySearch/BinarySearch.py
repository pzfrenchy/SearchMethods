list = [4,9,12,13,18,27,53]

def Search(l, t):
    found = False
    start = 0
    end = len(l)-1
    while start <= end and not found:
        mid = (start + end)//2
        if l[mid] == t:
            found = True
        else:
            if t < l[mid]:
                end = mid - 1
            if t > l[mid]:
                start = mid + 1
    return found

term = int(input("Please enter a search term: "))
result = Search(list, term)
if result == True:
    print("term found")
elif result == False:
    print("term not found")