import json

input = '''[
    {"id" : "001",
    "x" : "2",
    "Name" : "Chuck"
    },
    {"id" : "002",
    "x" : "3",
    "Name" : "Sandra"
    }
]'''

info = json.loads(input)
print('Items: ', len(info))

for value in info:
    print('Name: ', value["Name"])
    print('Id: ', value['id'])
    print('Value: ',value['x'])
