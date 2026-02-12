# memanggil function
def my_function():
  print("Hello from a function")

my_function()


def my_function(name = "liya"):
  print("Hello", name)

my_function()


def my_function(name):
    print("Hello", name)

my_function("liya")


#scope python
def myfunc():
  x = 300
  print(x)

myfunc()


#variabel di luar fungsi
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#variabel lokal fungsi dalam fungsi
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


#python lambda
x = lambda a : a + 10
print(x(5))


#rekursi python
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))


#fibonacci
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
