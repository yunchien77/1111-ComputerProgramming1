height = float(input())
weight = float(input())
newheight = height / 100
bmi = weight / (newheight ** 2)
print("%.1f" %bmi)