def greet2(name):
    print("반갑습니다",name)
    print(name, "님은 파이썬의 세계로 오셨습니다.")

def adder(num1, num2):
    print("덧셈 결과:", num1+num2)

adder(2,3)

def three_times(text):
    print(text,text,text)

three_times("사랑해")

def change(num1):
    print("전환결과:",-(num1))

change(1)
change(-1)

def average(num1,num2):
    print("평균:",(num1+num2)/2)

average(2,4)
average(4,4)
average(3,4)

def adder2(num1,num2):
    ar=num1+num2
    return ar

result = adder2(4,8)
print(result)

def change2(num1):
    ch=-num1
    return ch
result=change2(1)
print(result)

def change2(num1):
    ch=-num1
    return ch
result=change2(-2)
print(result)

# 200726_1.py
def average2(num1,num2): # 함수 average2의 정의
    av=(num1+num2)/2 # num1과 num2의 평균값을 구함
    return av
result=average2(3,3) # num1과 num2의 값을 넣어 average2 함수를 구동하고 그 결과를 남김
print(result) # result 결과 호출

#adder1 main함수 없이
def adder1(num1, num2): #adder1 함수의 정의
    return num1+num2

print(adder1(5,3)) #위에 정의된 adder1 함수의 호출과 print 함수의 호출

#adder2 main함수 있게
def adder2(num1,num2,num3): #adder2 함수의 정의
    return (num1+num2)-num3

def main(): #프로그램의 실행 흐름을 담은 main 함수의 정의
    print(adder2(1,2,3))

main() #위에 정의된 함수 main의 호출

#멀티 함수 정의
def add(num1,num2): #add 함수의 정의
    return num1+num2
def min(num1,num2): #min 함수의 정의
    return num1-num2
def mul(num1,num2): #mul 함수의 정의
    return num1*num2
def div(num1,num2): #div 함수의 정의
    return num1/num2

def main():
    print(add(2,2))
    print(min(2,2))
    print(mul(2,2))
    print(div(2,2))

main()

main()
main()


