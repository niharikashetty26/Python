age = 30
name = "Niharika"
height = 5.9
is_employed = True
hobbies = ["reading", "coding", "hiking"]
coordinates = (40.7128, 74.0060)
person = {
    "name": "Niharika",
    "age": 24,
    "hobbies": hobbies,
    "coordinates": coordinates,
    "is_employed": is_employed
}

print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Is Employed: {is_employed} (Type: {type(is_employed)})")
print(f"Hobbies: {hobbies} (Type: {type(hobbies)})")
print(f"Coordinates: {coordinates} (Type: {type(coordinates)})")
print(f"Person: {person} (Type: {type(person)})")
