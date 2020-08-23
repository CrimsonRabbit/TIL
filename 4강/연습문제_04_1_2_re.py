#연습문제 04-1 문제2
def bet_sum(n1,n2):
    n1=int(n1)
    n2=int(n2)
    sum=0
    for i in range(n1+1,n2):
        sum=sum+i
    print(sum)

