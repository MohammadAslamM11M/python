a = 31
print(type(a))  # <class 'int'>

b = 31.4
print(type(b))  # <class 'float'>

c = "31.4"
print(type(c))  # <class 'str'>

d = float(c)    # str is converted into float (works only in valid conversions)
print(d)