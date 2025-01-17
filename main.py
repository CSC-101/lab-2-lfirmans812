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
second = smallest(2, 2)    #What is the value of second? Is this a reasonable result? Why or why not The value of
                                 # the second is 2 and this is reasonable because the only criteria is for n < m,
#                                which it is not because the values are equal.
print()

def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b      # In general, when will a call to this function evaluate this statement? This statement will be
                        # evaluated when a > b and a > c.
   elif b > c:
      return b + c      # In general, when will a call to this function evaluate this statement? This statement will be
                        # evaluated when b > c.
   else:
      return 2 * c      # In general, when will a call to this function evaluate this statement? This statement will be
                        # evaluated when a > b,  a > c, and b > c.

answer1 = function2(3, 2, 1) #What is the value of answer1? answer1 = 1
answer2 = function2(2, 3, 1) #What is the value of answer2? answer2 = 4
answer3 = function2(2, 1, 3) #What is the value of answer3? answer3 = 6
print()

from typing import Optional

def checked_accesss(L:list[int], idx:int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)    #What is the value of test on each call?
   if test:          #What is the check preventing?
      return L[idx]
   else:
      return None

first = checked_accesss([1, 0 ,1], 9)   #What is the value of first? None
second = checked_accesss([1, 0 ,1], 2)    #What is the value of second? 1
print()


def length_sum(L: list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])  # For which call below is this statement evaluated. This statement is
                                    # being evaluated for the call length_sum(["this", "is", "the", "first", "call"]).
   elif len(L) > 1:  # and what are the values being added? For length_sum(["this", "is", "the", "first", "call"]),
                     # the values 4 + 2 + 3 are being added.
      result = len(L[0]) + len(L[1])  # For which call below is this statement evaluated? This statement is being
                              # evaluated for the call length_sum(["another", "call"]).
   elif len(L) > 0:  # and what are the values being added? For length_sum(["another", "call"]), the values 7 + 4
                     # are being added.
      result = len(L[0])   # For which call below is this statement evaluated. This statement is being evaluated for
                           # length_sum(["second call"]).
   else:                   # and what are the values being added? The value being added is 11.
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()


def surprising(L: list[str], other: str) -> list[str]:
   L.append(other.upper())
   return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# What is the value of words at this point? words = ['this', 'is', 'confusing', 'code.', 'AVOID,' 'SUCH.']
# What are the values of first and second at this point? first and second = ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
# What happened? The list words was appended with fully uppercased strings "Avoid" and "such."because of the surprising
# function that has L.append and other.upper.
print(first)



