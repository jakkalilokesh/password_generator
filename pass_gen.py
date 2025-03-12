import random
import string

l1 = list(string.ascii_uppercase)
l2 = list(string.ascii_lowercase)
l3 = list(string.digits)
l4 = list(string.punctuation)

user_input = input("How many characters do you in your password: ")

while True:
    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print("Your number should be at least 8.")
            user_input = input("Please, Enter Your number again:")
        else:
            break
    except:
        print("Please, Enter numbers only.")
        user_input = input("How many characters do you in your password: ")

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)
random.shuffle(l4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
result = []

for x in range(part1):
    result.append(l1[x])
    result.append(l2[x])

for x in range(part2):
    result.append(l3[x])
    result.append(l4[x])

random.shuffle(result)
password = "".join(result)
print("Your Strong Password is: ",password)