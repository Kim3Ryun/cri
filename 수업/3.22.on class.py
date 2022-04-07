#구의 겉넓이와 부피

def ball_vol(r):
    
    print("#구의 겉넓이 & 부피")
    print("-"*25)
    print()
    pi = 3.141592
    print()
    out_area = 4*pi*r**2 #구의 겉넓이 모델
    print("out_area = 4*pi*r**2 : 구의 겉넓이 모델")
    print()
    print("구의 겉넓이:", round(out_area,2))

ball_vol(40)
