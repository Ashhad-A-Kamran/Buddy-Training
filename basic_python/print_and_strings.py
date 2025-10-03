
#Task1
# print("Name: ashhad", "Age: 22", "City: Karachi", sep="|")

#Task 2
# for i in range(0,6):
#     print(i, end=",")
    


#Task 3
registration, monthly, months = int(input("Enter registration fee: ")), int(input("Enter monthly fee: ")), int(input("Enter number of months: "))

total = registration + (monthly * months)
print(f"total fee before discount: {total}")

discount_coupon = bool(input("Do oyu have a discount coupon? (True/False): "))


if discount_coupon:
    total = total * 0.90
    print(f"Total fee after discount: {total}")
    
else:
    print(f"Total fee to be paid: {total}")

# Task4

# photo = input("Photo (True/False): ")
# id_card = input("ID Card (True/False): ")
# sign = input("Sign (True/False): ")

# valid = photo=="True" and id_card=="True" and sign=="True"
# print(valid)

#Task 5

# balance = 0

# want_to_add = float(input("How much money do you want to add? "))
# balance += want_to_add
# print(f"Your current balance is: {balance}")

# spent_on_food = float(input("How much did you spend on food? "))
# balance -= spent_on_food

# spent_on_transport = float(input("How much did you spend on transport? "))
# balance -= spent_on_transport  

# spent_on_shopping = float(input("How much did you spend on shopping? "))
# balance -= spent_on_shopping

# valid_balance = balance > 500 and balance <= 5000
# print(valid_balance)


# print(f"Your remaining balance is: {balance}")