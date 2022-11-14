from turtle import *

speed('fastest')
i = 1
while True:
    fd(10 + i)
    for j in range(6):
        fd(i)
        lt(360/6)
    left(360/6)
    i += 5
    write(i)
    
    if i > 500:
        break
mainloop()