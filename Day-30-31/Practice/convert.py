def convert(s):
    try:
        return int(s)
    except ValueError:
        return "Cannot convert to int"

    
print(convert("abc"))
print(convert(1234))


