text = input()

if text == 'dog':
    animal = 'mammal'
elif text == 'crocodile' or text == 'tortoise' or text == 'snake':
    animal = 'reptile'
else:
    animal = 'unknown'

print(animal)
