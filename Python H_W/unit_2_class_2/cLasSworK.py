count = 0 
while count<21:
    print(count)
    count += 1

print("------------------------------------")

pak_drama = ["Humsafar", "Kabhi main kabhi tum", "Ishqiya", "meem se mohobat", "ghair"]
seen = []
while pak_drama:
    name = pak_drama.pop()
    seen.append(name)
print(pak_drama, seen)

print("-------------------------------------")

unliked_food = ['pangash', 'korola', 'oil', 'mas er tel','pangash', 'meat er tel']

while "pangash" in unliked_food:
    unliked_food.remove('pangash')

print(unliked_food)

print("-------------------------------------")

# Clear = ctrl + L
# to turn off the infinite loop = Ctrl + C

print("ek din marjayega...... ki mot")