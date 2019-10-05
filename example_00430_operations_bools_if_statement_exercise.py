# you have 2 numbers, 5 and 10
# if the first is bigger than the second, print bigger
# if the second is bigger, print smaller
# otherwise print equal
x=5
y=10
if x > y:
    print("bigger")
elif x < y:
    print("smaller")
elif x==y:
    print("equal")

# you have a variable called "age"
# if age is smaller than 2, print baby
# if age is between 2 and 18, print kid
# otherwise print adult
age=int(input("Bitte Alter eingeben: "))
if age < 2:
    print("baby")
elif age>2 and age<18:
    print("adult")


