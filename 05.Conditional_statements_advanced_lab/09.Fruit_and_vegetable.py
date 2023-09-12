product = input()

list1 = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
list2 = ['tomato', 'cucumber', 'pepper', 'carrot']

if product in list1:
    print('fruit')
elif product in list2:
    print('vegetable')
else:
    print('unknown')
