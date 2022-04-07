#input을 이용하여 원의 둘레와 넓이 구하기(20226717 김세륜)
r = input("반지름")
pi = input("원주율")
cle = 2*int(r)*float(pi)
area = float(pi)*int(r)**2
print("원의 반지름:",int(r))
print("원의 둘레:","%.2f"%(cle))
print("원의 넓이:",format(area,".2f"))
