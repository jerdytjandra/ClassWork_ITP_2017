favorite_places = {'jane': ['bali','paris','tokyo'],
                   'alexa': ['miami','london'],
                   'mary': ['rio','lyon','rome']
                   }
print(favorite_places)

for name in favorite_places.keys():
    print(name.title())

for favorite_place in favorite_places.values():
    print(favorite_place)

for name,cities in favorite_places.items():
    print("\n" +name.title() + "'s favorite cities are:")
    for city in cities:
        print("\t" + city)
