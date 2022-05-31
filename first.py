x = 2 + 3
y = 8
z= x * y
name = 'obinna'
print(z)
print(name)
print(type(x))
print(type(name))
print(y/x)
print(type(y/x))
print(type([5,6]))
print(type({'a':'John','b':20}))
def square(x):
  print(x*x)
square(5)
def exponent(x,y):
  print (x**y)  
exponent(2,3)
print(name[1:7])
print(len(name))
scores = [1,2,3,4,5,6,7]
even = scores [1::2]
odd = scores [::2]
print(even)
print(odd)
x = 0
while x < 10:
  print(x)
  x = x + 1 
for x in range(8):
  print(x)
def my_sum(x,y):
  return x+y
x = my_sum(1024,1024)
print(x)
def is_even(x):
  if x % 2 == 0:
    return True
  return False
print(is_even(8))
def is_odd(x):
  if x // 2 != 0:
    return False
  return true
print(is_odd(8))

def is_prime(x):
  first_5 = [2,3,5,7,11]
  if x < 12:
    if x in first_5:
      return "prime"
    return " not prime"
  for y in first_5:
      if x % y == 0:
        return "not prime"
  return "prime"
for z in range(30):
  print(f"{z} is: {is_prime(z)}")

def is_prime(x):
  for y in range (x):
    if x % y == 0:
      return "not prime"
  return "prime"
print(is_prime(20))
