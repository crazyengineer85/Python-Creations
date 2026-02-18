x = ["BMW","Mercedes", "Opel", "Mazda"]
print(x)
print(len(x))
print(f"ilk = {x[0]} enson = {x[-1]}")
x[-1] = "TOYOTA"
print(x)
y = 'Mercedes' in x
print(y)
y = 'ReNAULT' in x
print(y)
print(x[-2])
print(x[:3])
x[-2] = "TOYOTA"
x[-1] = "ReNAULT"
print(x)
x = x + ["AUDI", "nissan"]
print(x)
x.pop()
print(x)
print(x[::-1])

# Aşağıdaki verileri bir listede sakla

# studentA: A 2010, (70,60,70)
# studentB: B 1999, (80,80,70)
# studentC: C 1998, (80,70,90)

x = "studentA: A 2010, (70,60,70)".split()
y = "studentB: B 1999, (80,80,70)".split()
w = "studentC: C 1998, (80,70,90)".split()


students = [x]+[y]+[w]

print(students)