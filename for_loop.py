"""
working on for loops

"""

cities = ["london", "new york", "madrid", "paris", "ogden"]

# iterate over this collection/list

for city in cities:
    print(city)


d = {'alice':'801-123-45-8998',
     'pedro': '956-445-78-8996',
     'john':'654-321-66-4477'}

#iterate over a dictionary

for item in d:
    print(item, "=>", d[item])