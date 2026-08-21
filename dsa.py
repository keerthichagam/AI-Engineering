#find largest element
numbers=[5,12,8,20,3,15]
largest=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]
print(largest)
#find smallest number
numbers=[12,5,18,3,25,7]
smallest=numbers[0]
for x in numbers:
    if x<smallest:
        smallest=x
print(smallest)
#counting
numbers=[5,12,8,20,3,15]
count=0
for i in numbers:
    if i>10:
        count+=1
print(count)
#sum of array
numbers=[5,12,8,20,3,15]
total=0
for i in numbers:
    total+=i
print(total)
#linear search
numbers=[5,12,8,20,3,15]
target=20
found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        found=True
        break
if found:
    print("Element found at index",i)
else:
    print("Not Found")
#Binary search
numbers=[1,3,5,7,9,11,13]
target=3
left=0
right=len(numbers)-1
while left<=right:
    mid=(left+right)//2
    if numbers[mid]==target:
        print("Element found at index",mid)
        break
    elif numbers[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Element not found")
#binary search example
numbers=[-1,0,3,5,9,12]
target=9
left=0
right=len(numbers)-1
while left<=right:
    mid=(left+right)//2
    if numbers[mid]==target:
        print("Elements found at index",mid)
        break
    elif numbers[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Element not found")
#Two pointer
numbers = [2, 3, 4, 7, 11, 15]
target = 9
left=0
right=len(numbers)-1
while left<right:
    current_sum=numbers[left]+numbers[right]
    if current_sum==target:
        print("Pair found",numbers[left],numbers[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1