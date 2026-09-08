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
#hashing technique
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        print([seen[complement], i])
        break
    seen[num] = i
nums = [3, 2, 4]
target = 6
seen={}
for i, num in enumerate(nums):
    complement=target-num
    if complement in seen:
        print([seen[complement],i])
        break
    seen[num]=i
#duplicates
nums = [1, 2, 3, 1]
seen = set()
for num in nums:
    if num in seen:
        print("Duplicate found:", num)
    seen.add(num)
#valid anagram
s = "anagram"
t = "nagaram"
freq_s = {}
freq_t = {}
for char in s:
    freq_s[char] = freq_s.get(char, 0) + 1
for char in t:
    freq_t[char] = freq_t.get(char, 0) + 1
if freq_s==freq_t:
    print(True)
else:
    print(False)
#window sliding techique
nums = [2, 1, 5, 1, 3, 5]
k = 3 
window_sum = sum(nums[:k])
max_sum=window_sum
for i in range(k, len(nums)):
    window_sum += nums[i] -nums[i-k]
    max_sum=max(max_sum,window_sum)
print(max_sum)
#linear search example
products = [105, 203, 310, 415, 502]
target = 415
found=False
for i in range(len(products)):
    if products[i]==target:
        found=True
        break
if found:
    print("Product found at index:",i)
else:
    print(("Product not foound"))
#example
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
nums = [4, 7, 1, 9, 3]
target = 10
index=linear_search(nums,target)
if index!=-1:
    print("Element found at index:",index)
else:
    print("Element not found")
#binary example
nums = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target=56
left = 0
right = len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print("Element found at index", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
            right = mid - 1
else:
    print("Element not found")  