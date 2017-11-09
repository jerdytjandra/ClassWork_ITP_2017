cities = {'paris': {
            'country': 'france',
            'population': '2 400 000'},
          'rome': {
            'country':'italy',
            'population': '2 800 000'}
        }

for city, city_info in cities.items():
    print("City: " + city.title())
    country_name = city_info['country']
    population_info = city_info['population']
    print("\tCountry: " + country_name.title())
    print("\tPopulation: " + population_info.title())
