import json

data = '''{
    "name" : "Chuck",
    "phone": {
                "type" : "intl",
                "number": "+1 245 478 653"
    },
    "email": {
                "hide" : "yes"
                }
    }'''

toString = json.loads(data)
print(toString["name"])
print(toString["phone"])
print(toString["email"]["hide"])
