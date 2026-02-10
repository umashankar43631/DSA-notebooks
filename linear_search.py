ls1 = [1,2,2,34,1,45,12,34,1]

def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

result = linear_search(ls1, 45)
if result:
    print("Element found")
else:
    print("Element not found")
    print("Thanks")