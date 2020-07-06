# Python knows a number of compound data types, used to group together other values.

squares = [1, 4, 6, 7, 8]

print(squares)

print(squares[0])

print(squares[:])

print(squares[-3:])

a = 4 ** 3

squares[3] = a

print(squares)

squares.append(100)

print(squares[:])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters)

print(letters[2:5])

print(letters[:])

print(len(letters))

a = ['a', 'b', 'c']

n = [1, 2, 3]

x = [a, n]

print(x)

print(x[0])

print(x[0][1])

x, y = 0, 1
while x < 10:
    print(x)
    x, y = y, x + y