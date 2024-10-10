print("a"<"b")
print("b"<"a")
print("John" < "Jerry")
print([1,2,3]<[1,2,3])
print([1,2,2]<[1,2,3])
print(5<10.2)

print(5<6)

print(5 == "5")

age = int(input("enter your age: "))
print(18 == age)



print(age >=18 and age <=65)
print(age <18 or age >65)

print((age >=18 and age <=65) and (not age==30))


print(18 < age <= 65)
print( age and age <= 65)

print(18 < age <= 65)
print(18 < age and age <= 65)
weight = 150
print(100 < weight and weight < 200)
height = 140
print(height > 131 and height < 200)


names = ["terry","john","michel","eric","terry", "graham"]
print("eric" in names)

print("mark" not in names)


message = "hello there, my name is john"
print("nam" in message)

if age > 100:
    print("you are a big man")
    print("your smelly")

if age > 100:
    print("you are a big man")
    print("your smelly")
else:
    print("go buy beer")

if age > 100:
    print("you are a big man")
    print("your smelly")
elif age > 80:
    print("you are a bean man")
    print("bugger")
elif age > 40:
    print("you are a toad man")
    print("your a scooter kid")
else:
    print("wanker")
Total = 45
if Total:
    print("total is non-zero")
else:
    print("total is zero")
name = input("enter your name: ")
if name:
    print("your name is", name)
else:
    print("name not entered")


if Total != 0:
    print("your total is", Total)