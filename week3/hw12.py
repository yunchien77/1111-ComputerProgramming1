temperature = int(input())
humanity = int(input())
wind = int(input())

def op(t, h, w):
    if (t >= 50):
        print('18')
    elif (t < 25):
        print('Today is cool')
    elif ((t >= 30) and (w == 0)) or (h >= 85):
        print('24')
    elif ((25 <= t <= 29) and (60 <= h <= 84) and (w == 1)) or ((25 <= t <= 29) and (h < 60) and (w == 0)):
        print('27')
    else:
        print('Today is cool')
        
op(temperature, humanity, wind)