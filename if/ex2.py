## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#Write a program that asks user to enter two cities and it tells 
# you if they both are in same country or not. For example if I enter 
# mumbai and chennai, it will print "Both cities are in India" 
# but if I enter mumbai and dhaka it should print "They don't belong to same country"

user= []

user.append(str(input("Enter 2 cities: ")))
user.append(str(input("")))
print(user)

india = ["mumbai", "mumbai", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

if (user[0]in india and user[1]in india):
    print("Both cities are in India")
elif (user[0] in pakistan and user[1]in pakistan) :
    print("Both cities are in Pakistan")
elif (user[0]in bangladesh and user[1]in bangladesh):
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")