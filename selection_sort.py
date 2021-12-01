# Selection Sort
n = int(input("Enter the number of elements in the list"))
lst = list(map(int, input("Enter the elements of the list seperated by space").split()))[:n]
for i in range(n):
        index = i
        for j in range(i+1,n-1):
            if lst[j]<lst[index]:
                index = j
        lst[i],lst[index] = lst[index],lst[i]
print("The Sorted List is: ",lst)
