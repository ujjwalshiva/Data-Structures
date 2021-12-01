#bubble sort
n = int(input("Enter the number of elements in the list"))
lst = list(map(int, input("Enter the elements of the list seperated by space").split()))[:n]
for i in range(n):
    for j in range(n):
        if lst[i]<lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print("The Sorted List is: ",lst)
