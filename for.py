# #ex1
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count = 0 
# for i in range(0 , len(result) + 1):
#     if "head" in result[i]:
#         count +=1
# print(count)

# #ex2: Print square of all numbers between 1 to 10 except even numbers
# for i in range(1, 11):
#     if i %2 != 0:
#         print(i* i)

# # ex3: 
# user = int(input())
# expense_list = [2340, 2500, 2100, 3100, 2980]
# for i in range(0 , len(expense_list)):
#     if user == expense_list[i]:  
#         print(i + 1)

# ex 4: Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

# for i in range(0, 5):
#     print("are you tired?")
#     user = str(input())
#     if(user == "yes"):
#         print("you didn't finish the race")
#         break

#     if(i == 4): 
#         print("congratulations")
    


# ex 5 
# for i in range(1 , 6):
#     print("*" * i )