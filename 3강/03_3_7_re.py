#연습문제03-4 문제3 다시풀이
def exp(n1,n2):
    n1=int(n1)
    n2=int(n2)
    sum=0
    for i in range(n2):
        exp_result=n1*n1
        sum=exp_result*i
        print(sum)

