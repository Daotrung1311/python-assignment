d = {
    "China" : 143,
    "India" : 136,
    "USA" : 32,
    "Pakistan" : 21
}
user = input()
if user == "":
    for key in d:
        print(f"{key}==>{d[key]}")
elif user == "add":
    country = input("Enter a country name to add: ")
    if country in d:
        print("country is exiting in dictionary")
    else:
        poluation = int(input(f"Enter population of {country}: "))
        d[country] = poluation
        print(d)
elif user == "remove":
    country = input("Enter a country name to remove: ")
    if country in d:
        del d[country]
        print(d)
    else:
        print("that country doesn't exist")
elif user == "query":
    country = input("country you want to query: ")
    if country in d:
        print(f"{country}==>{d[country]}")
    else:
        print("that country doesn't exist")
else:
    print("Invalid input")