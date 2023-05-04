# json

import json

# python object converting to json
employee = {'name': 'John', 'age': 31, 'salary': 25000}
print(json.dumps(employee))

# json object converting to python
employee = '{"name": "John", "age": 31, "salary": 25000}'
print(json.loads(employee))

var = {
    'Subjects': {
        'Maths': 85,
        'Physics': 90
    }
}
with open('sample.json', 'w') as f:
    json.dump(var, f)

json_var = '''
{
    "country": {
        "name": null,
        "languages_spoken": [
            {
                "names": ["English", "Spanish"]
            }
        ]
    }
}
'''
