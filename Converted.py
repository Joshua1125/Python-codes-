a = 12
b = 3
c = 6
d = 2

f1 = float(a+(b/c)-(d*d))
f2 = float(((a+b)/c)-(d*d))
f3 = float(a + (b/(c-(d*d))))
f4 = float((a + b)/(d*d))

print("The value of f1 is " + str(f1))
print("The value os f2 is " + str(f2))
print("The value of f3 is " + str(f3))
print("The value of f4 is " + str(f4))
