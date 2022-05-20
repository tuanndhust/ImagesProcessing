a = ['1','2','3']
b = []
for i in range(3):
    a[i] = int(a[i])
    b.append(a[i])
print(b)