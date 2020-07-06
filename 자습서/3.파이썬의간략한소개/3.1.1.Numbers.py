# Simple Calculator
# Python Console

a = 2+2
print(a)
print(type(a))    # class int

b = 50 - 5*6
print(b)
print(type(b))    # class int

# Division (/) always returns a float

c = (50 - 5*6) / 4
print(c)
print(type(c))    # class float

d = 8 / 5
print(d)    # result = 1.6
print(type(d))    # class float

# To do floor division(//) and get an integer result

e = 17 // 3
print(e)
print(type(e))

# the % operator returns the remainder of the division

f = 17 % 3
print(f)
print(type(f))

# Use the ** operator to calculator powers

g = 5 ** 2
print(g)

# equal sign is used to assign a value to a variable
width = 20
height = 5 * 9
print(width * height)

print(4 * 3.75 - 1)     # 14.0

tax = 12.5 / 100
price = 100.50
h = price * tax
print(h)
print(h + price)
print(round(h+price, 2))