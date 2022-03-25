from classes import Budget

food = Budget(int(input("Please enter your budget for food: ")), "Food")
food.categories = "Food" 

clothes = Budget(int(input("Please enter your budget for clothes: ")), "clothes")
clothes.categories = "Clothes"

entertainment = Budget(int(input("Please enter your budget for entertainment: ")), "entertainment")
entertainment.categories = "Entertainment"

def transfers(budget1, budget2):
    t_amount =  int(input("Enter the amount you'd like to transfer: "))
    budget1.withdraw(t_amount)
    budget2.deposit(t_amount)
    return [t_amount, budget1, budget2]

def transaction_amount(t_amount, category1, category2):
    with open("transactions.txt", "r") as file1:
        contents = file1.readlines()
    with open("transactions.txt", "w") as file1:
        for items in contents:
            file1.write(items)
        trans_amount = "You transferred "  + str(t_amount) + " from " + category1.categories + " to " + category2.categories + "\n"
        file1.write(trans_amount)

def transcations(category):
    with open("transactions.txt", "r") as file1:
        contents1 = file1.readlines()
    with open("transactions.txt", "w") as file1:
        for item in contents1:
            file1.write(item)
        statement = category.categories + "@" + str(category.amount) + "\n"
        file1.write(statement)
    

transfer_string = f'list1 = transfers({input("From which budget would you like to transfer money?")}, {input("And to which budget?")})'
exec(transfer_string)

print(food, clothes, entertainment)

transaction_amount(list1[0], list1[1], list1[2])
transcations(food)
transcations(clothes)
transcations(entertainment)


