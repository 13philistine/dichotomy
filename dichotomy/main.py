# coding: cp866
e = float(1e-5)
a = 0
b = 16

def f(x):
    return (pow(x,3)) - 13

print("Посчитать к-во шагов, когда на отрезке будет E")
print("E=", e)
#x^5=1613
fout = open('output.txt', 'w')
print("a= ", a,"  b= ", b, "  (b-a)= ", (b-a), "  Итого=", (a+b)/2, file=fout )
print("f(a)=", f(a), "  f(middle)=", f((a+b)/2), "\n", file=fout)
print("a= ", a,"  b= ", b, "  (b-a)= ", (b-a), "  Итого=", (a+b)/2)
print("f(a)=", f(a), "  f(middle)=", f((a+b)/2))
while b - a > e:
    c = (a + b) / 2
    if f(c) >= 0:
        b = c
    else:
        a = c
    print("a= ", a,"  b= ", b, "  (b-a)= ", (b-a), "  Итого=", (a+b)/2, file=fout )
    print("f(a)=", f(a), "  f(middle)=", f((a+b)/2),"\n", file=fout)
    print("a= ", a,"  b= ", b, "  (b-a)= ", (b-a), "  Итого=", (a+b)/2)
    print("f(a)=", f(a), "  f(middle)=", f((a+b)/2),"\n")
fout.close()