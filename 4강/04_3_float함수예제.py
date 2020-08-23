#float함수의 사용(1)
num=10
num=float(num)
type=type(num)
print(type,num)

#float함수의 사용(2) (1)과 같이 돌리면 3.14 3.14로 나옴. *함수는 한 파일에 하나씩만 저장할 것.
num="3.14"
num=float("3.14")
type=type(num)
print(type,num)

#float함수의 사용(3)
height=eval(input("키 정보 입력:"))
print(height)

#float함수의 사용(4)
height=float(input("키 정보 입력:"))
print(height)
