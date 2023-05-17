import random


defen=0
jisu=0
while jisu<3:
    jisu+=1
    suiji1 = random.randint(1, 10)
    suiji2 = random.randint(1, 10)
    jieguo = suiji1 + suiji2
    suru1=float(input("请输入"+str(suiji1)+"+"+str(suiji2)+"=："))

    if suru1==jieguo:
        defen+=10
    else:
         defen-=5



print("总分是："+str(defen))