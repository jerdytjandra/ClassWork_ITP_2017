##4-1 and 4-11##
pizzas=['mushroom', 'beef', 'pepperoni']
print('The first three types of pizzas are:')
for pizza in pizzas[:]:
    print(pizza.title())

print('\n' +'These are the choices of my friend:')
pizza_friend=pizzas
print(pizza_friend)

print('\n' +"My friend's new choices are:")
pizza_friend.append('macaroni')
print(pizza_friend)

print('\n' +"My new  choices are:")
pizzas.append('cheese')
print(pizzas)

for pizza in pizzas:
    print('\n' + 'I like ' + pizza + ' pizza.')
    print(pizza.title() + ' pizza is really delicious.' +'\n')

print('I like pizza.')

print('\n' + '--------------------------------------')

##4-2 and 4-10##
animals = ['lion', 'bear', 'wolf', 'coyote']
print('\n' + 'The first three animals are:')
for animal in animals[:3]:
    print(animal.title())

print('\n' + 'The three animals from the middle of the list are:')
for animal in animals[1:3]:
    print(animal.title())

print('\n' + 'The last three items in the list are:')
for animal in animals[1:]:
    print(animal.title())

for animal in animals:
    print('\n' + 'A ' + animal.title() + ' is a carnivore.')
    print('A '+ animal.title() + ' is not a very friendly animal.')


