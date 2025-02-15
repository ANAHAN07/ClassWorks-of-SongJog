num = [2,4,6]
for num in num:
    print(num * 3)


# practice 1
word = "hello"

for letter in word:
    print(letter)

print("----------------")

# practice 2 
word = "Uchiha Madara"
vowels = "aeiou"  
vowel_count = 0

for letter in word:
    if letter in vowels:  
        vowel_count += 1

print("Number of vowels:", vowel_count)

print("----------------")

for i in range(6,15):
    print(i)

print("----------------")

for num in range(1, 11):
   print(num)

print("----------------")

for num in range(2, 21, 2):
   print(num)

print("----------------")

