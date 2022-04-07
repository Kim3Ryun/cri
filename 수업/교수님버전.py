pi = float(input("원주율"))
r = int(input("원의 반지름"))
cle = 2*pi*r
area = pi*r**2
print("원의 반지름:" ,r)
print("원의 둘레:", "%.2f"%(cle))
print("원의 넓이:", format(area,".2f"))
