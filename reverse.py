import timeit
a=input("enter")
b=timeit.default_timer()
print("start",b)
def reverse(a):
    if len(a) == 0:
        return a
    else:
        return reverse(a[1:]) +a[0]
print(reverse(a))
d=timeit.default_timer()
print("end",d)
print(d-b)