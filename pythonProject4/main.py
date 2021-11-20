# 3.1 считает 4 числа c клавиатуры и выведет на экран самое большое из них
t, y, z, k = (int(input("t="))), (int(input("y="))), (int(input("z="))), (int(input("k=")))
if t > y and y > z and z > k:
    print(t)
elif y > z and y > k:
    print(y)
elif z > k:
    print(z)
else:
    print(k)