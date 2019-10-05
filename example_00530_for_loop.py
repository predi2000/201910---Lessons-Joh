# for loop mit break, wenn number > 50 break
# number * 5 nach jedem loop
# range(1,20)


for i in range(1,21):
    i = input("Bitte i eingeben: ")
    number=int(i)*5
    if number > 50:
        break
    print(number)


