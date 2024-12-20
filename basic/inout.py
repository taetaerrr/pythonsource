# 화면 입출력
print("T", "E", "S", "T") # T E S T
print("T", "E", "S", "T",sep="" ) # TEST

print("Life is too short",end=" ")
print("You need Python")

print("2024","12","20",sep="-")

# 문자열 포매팅
# %d : 정수, %f : 부동소수, %c : 문자 1개, %s : 문자열

#  I eat 3 apples
apple = 3
print("I eat",apple,"apples")
print("I eat %d apples" % apple)

msg = "I eat %d apples" % apple
print(msg)

print("Error is %d%%" % 98)

number = 10
day = "three"
msg = "I ate %d apples, so I was sick for %s days" % (number, day)
print(msg)

# 포맷코드와 숫자 함께 사용
print("%s" % "hi")
print("%10s" % "hi") # 전체 길이가 10이고 오른쪽 정렬하고 나머지는 공백
print("%-10sjane" % "hi") # 전체 길이가 10이고 왼쪽 정렬하고 나머지는 공백

# 소수점 4번째 자리까지 출력

# "".format()
msg = "I eat {} apples".format(apple)
print(msg)

msg = "I ate {} apples, so I was sick for {} days".format(number, day)
print(msg)

# f 문자열 포매팅
msg = f"I ate {number} apples, so I was sick for {day} days"
print(msg)

# 키보드 입력
# input()
# print("숫자 입력")
# msg = input()
# print(msg)

# msg = input("숫자 입력 : ")
# print(msg)


# 숫자 2개를 입력 받은 후 연산 작성
num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))
print(num1 + num2)



































