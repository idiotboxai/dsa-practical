def binarySearch(list1,x,low,high):
    while low <= high:
        mid = low+(high-low)//2
        if list1[mid] == x :
            return mid
        elif list1[mid] < x:
            low = mid+1
        else:
            high = mid -1
    return -1
list1=[1,2,3,4,5,6,7,11]
x=int(input("enter the number"))
result =binarySearch(list1,x,0,len(list1)-1)
if result != -1:
    print("element is present at index=" + str(result))
else:
    print("not found")
