# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."
   return message


message = welcome_message("lfirmans@calpoly.edu")
print(message)

def smallest(n: float, m: float) -> float:
   if n < m:       #For which calls below is this statement evaluated? The return n statement is evaluated when n < m.
      return n
   else:
      return m

first = smallest(3, 2)     #What is the value of first? first = 2
second = smallest(2, 2)    #What is the value of second? Is this a reasonable result? Why or why not The value of the second is 2 and this is reasonable because the only criteria is for n < m, which it is not because the values are equal.
print()

def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b      # In general, when will a call to this function evaluate this statement? This statement will be evaluated when a > b and a > c.
   elif b > c:
      return b + c      # In general, when will a call to this function evaluate this statement? This statement will be evaluated when b > c.
   else:
      return 2 * c      # In general, when will a call to this function evaluate this statement? This statement will be evaluated when a > b,  a > c, and b > c.

answer1 = function2(3, 2, 1) #What is the value of answer1? answer1 = 1
answer2 = function2(2, 3, 1) #What is the value of answer2? answer2 = 4
answer3 = function2(2, 1, 3) #What is the value of answer3? answer3 = 6
print(answer1)
