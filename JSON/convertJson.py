import json

x  = {
    "name" : "Harsh",
    "age": 20,
    "type" : "sophomore" 
}

y = json.dumps(x)

print(y)