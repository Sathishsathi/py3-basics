a = "aaaabbbcccddeee"

b = {}

for i in a:
    if i in b.keys():
        b[i] += 1
    else:
        b[i] = 1

c = ""
for l in b.keys():
    c += l + str(b[l])

print(c)
