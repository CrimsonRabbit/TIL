#05-8 설명내용 실습
for i in [1,2,3]:
    print(i,end=' ')

for i in 'happy':
    print(i,end=' ')

#05-9 설명내용 실습
st=[1,2,3,4]
print(len(st))

st='hahaha~'
print(len(st))

st='hahaha~'
n=len(st)
print(n)

#05-10 설명내용 실습
def so_sim1(num):
    return num+1
n=so_sim1(9)
print(n)

def so_sim2(st):
    print(st)

def so_sim3():
    st=[1,2,3,4,5]
    return st
r=so_sim3()
print(r)

def so_sim4(s):
    print(s)
    return "bye~"
r=so_sim4("hello")
print(r)
