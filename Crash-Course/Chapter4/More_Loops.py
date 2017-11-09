foods=['rice', 'beef', 'vegetables', 'egg']
print('These are some types of foods:')
print(foods)

for food in foods[:]:
    print('\n' + 'I want to eat some')
    print(food.title())
    print('May I have some:')
    print(food.title())
