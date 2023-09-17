
A1Q1
userInput = input("Enter Hours: ")

try:
    hours = float(userInput)
    
    # 检查是否为大于0的数
    if hours < 0:
        print("Error, please enter a number greater than zero.")
        quit()

    if hours <= 20:
        income = hours * 20
    else:
        income = (20 * 20) + ((hours - 20) * 25)
    
    print("Pay: ", income)

except ValueError:  # 捕获ValueError异常，而不是所有异常
    print("Error, please enter numeric input")
    quit()

A1Q2
try:
    score = int(input("Enter your score: "))
    
    # 检查分数是否在0到100的范围内
    if score < 0 or score > 100:
        print("Error: Please enter a score between 0 and 100.")
    else:
        if score >= 90:
            print("Your rating is A")
        elif score >= 80:
            print("Your rating is B")
        elif score >= 70:
            print("Your rating is C")
        elif score >= 60:
            print("Your rating is D")
        else:
            print("Your rating is F")

except ValueError:  # 捕获ValueError异常，以处理非数字输入
    print("Error: Please enter a valid numeric input.")
A1Q3
x = [15,2.1,'Anna', ['red','yellow','blue']]

# 移除第一个元素
x.pop(0)

# 从列表里移除blue
x[2].pop()  

# 在列表里添加blue
x.append('blue')

print(x)
A1Q4
person_info = {
  "Mike": {"Favorite Language": "Java", "Age": 20},
  "Tracy": {"Favorite Language": "C++", "Age": 21},
  "Jack": {"Favorite Language": "Python", "Age": 19}
}

for name in sorted(person_info):
  print(name, person_info[name]["Favorite Language"], person_info[name]["Age"])
A1Q5
squares = []

for i in range(1, 21):
    if i % 2 == 0:
        squares.append(i**2)

print(squares) 
A1Q6
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}", end=" ")
    print()
