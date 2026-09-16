#dictionary
student={
    "name": "Keerthi",
    "age": 19,
    "grade": "A"
}
print(student["name"])
print(student["age"])
print(student["grade"])
student["age"]=20
print(student["age"])
student["city"]="New York"
del student["grade"]
if "name" in student:
    print("Name is present")
print(student.keys())
print(student.values())
print(student.items())
frequency = {}

frequency["apple"] = frequency.get("apple", 0) + 1
frequency["apple"] = frequency.get("apple", 0) + 1
frequency["banana"] = frequency.get("banana", 0) + 1

print(frequency)
numbers=[5, 12, 8, 20, 3, 15]
frequency={}
for num in numbers:
    frequency[num]=frequency.get(num,0)+1
print(frequency)
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