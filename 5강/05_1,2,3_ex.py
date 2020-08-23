#05-1 설명내용 실습
for i in [1,2,3]:
    print(i)

for i in [1,2,3]:
    print(i,end='_')

for i in [1,2,3]:
    print(i,end=' ')

#05-2 설명내용 실습
print([1, "hello", 3.3])

#05-3 설명내용 실습
print([1,2,3]+[4,5])
print([1,2,3]*2)

st=[1,2,3,4,5]
n1=st[0] #st[]안에 있는 숫자는 순서 5개 -> 0~4번째
n2=st[4]
print(n1,n2)

st=[1,2,3,4,5]
st[0]=5 #st[]안에 있는 숫자는 순서 5개 -> 0~4번째
st[4]=1
print(st)

st=[1,2,3,4,5]
print(st[-1],st[-2],st[-3])
