import json

data = '{"firstName": beyza nur, "lastName": kaya }'

y = json.loads(data) #stringi json datasina cevirme

print(y["firstname"])
print(y["lastname"])

customer = {
    "firstName": "beyza nur",
    "lastName": "kaya"
}

customerJson = json.dumps(customer) #python objesini json strignine cevirme

print(customer)