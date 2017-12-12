a = "abraham"
b = "lincon"

c = "mon,tue,wed,thu,fri,sat"

print(a.capitalize())
print(a.upper())
print(a.capitalize() + " " + b.capitalize())

print(c.replace(',','\n'))

print("Reverse of %s: " %(a) + a[::-1])
print(c.split(','))
