text = 'azcbobobegghakl'
count = 0
vowels = ['a','e','i','o','u']
for char in text:
    if char in vowels:
        count+=1

print("Number of vowels:",str(count))