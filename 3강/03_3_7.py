#연습문제03-4 문제3
num1=eval(input())
num2=eval(input())
exp=(num1,num2)
print(exp)
exp_result=num1*num1
for i in range(1,num2):
    exp_result=exp_result*i
    print("결과값=",exp_result)
#결과값은 나왔는데, 2*2*2... 같이 num2를 곱하기에 반영하는 방법을 모르겠어...
