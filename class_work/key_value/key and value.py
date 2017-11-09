pet_owner={'jane':1,
           'kim':'1',
           'lizzy':[1]
           }

for value in (pet_owner.values()):
    print(value)
pet_owner['lizzy'].append(2)
print(pet_owner['lizzy'])
