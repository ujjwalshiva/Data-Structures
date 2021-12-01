#Insertion Sort

n = int(input("Enter the number of elements in the list"))
lst = list(map(int, input("Enter the elements of the list seperated by space").split()))[:n]
for i in range(1,n):
    key = lst[i]
    j=i-1
    while j>0 and key<lst[j]:
        lst[j+1] = lst[j]
        j-=1
    lst[j+1] = key
print("The Sorted List is: ",lst)
