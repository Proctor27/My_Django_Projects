# Given a list of integers, return True if the sequence of numbers 1,2,3 
#appears in the list somewhere 

#1 arrayCheck([1,1,2,3,1]) - True
#1 arrayCheck([1,1,2,4,1]) - False
#1 arrayCheck([1,1,2,1,2,3]) - True

#Solution

def arraycheck(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False

question1 = arraycheck([1,1,2,3,1])
question2 = arraycheck([1,1,2,4,1])
question3 = arraycheck([1,1,2,1,2,3])
#print(question1)
#print(question2)
#print(question3)

# array = [1,1,2,4]
#for i in range(len(array)-1):
 #   if i == 1 and i+1 ==2 and i+2==3:
   #     print(True)


#Question 2
#Given a string, return a new string made of every other character starting with the first, so 'Hello' yields "Hlo"

#Stingbits('Hello')- 'Hlo'
#Stingbits('Hl')- 'H'
#Stingbits('Heeololeo')- 'Hello'

#solution

string = ('hello')
#print(string[::2])

def stringBits(mystring):
        return(mystring[::2])

        """
        result = ""
        for i in range(len(mystring)):
            if i%2 == 0:
            result = result +mystring[i]
        return result
        #this returns all the even placed strings
        """

No2_a = stringBits("Hello")
No2_b = stringBits('Hi')
No2_c = stringBits('heeololeo')
#print(No2_a)
#print(No2_b)
#sprint(No2_c)


#Question 3
#Given two stirngs, return True is either of the strings appears at the very end of the other string, ignoring upper/lower case differences
#(in other words, the computation should not be 'case sensitive').
#Note: s.lower() returns the lowercase version of a string.

#end_other('Hiabc', 'abc')
#end_other('AbC', 'HiaBC')
#end_other('abc', 'abXabc')

#solution
def end_other(a,b):
     a = a.lower()
     b = b.lower()
     return (b.endswith(a) and b.endswith(a))

No3_a = end_other('Hiabc', 'abc')
No3_b = end_other('AbC', 'HiaBC')
No3_c = end_other('abc', 'abXabc')
#print(No3_a)
#print(No3_b)
#print(No3_c)

def endstring(a,b):
     a = a.lower()
     b = b.lower()
     return a[-(len(b)):] == b or a == b[-len(a):]
dd = end_other('Hiabc', 'abc')
ee = end_other('AbC', 'HiaBC')
ff = end_other('abc', 'abXabc')
#print(dd)
#print(ee)
#print(ff)

#QUestion 4
#Given a string, return a string where for every char in the original, there are two chars
#doubleChar('The') - 'TThhee'
#doubleChar('AAbb') - 'AAAAbbbb'
#doubleChar('Hi-There) -> "HHii--TThheerree"

#SOlution

#loop the strings then double it
def doublechar(hundred):
     result = ""
     for num in hundred:
          result += num*2
     return result

     
no4_a = doublechar('The')
no4_b = doublechar('AAbb')
no4_c = doublechar('Hi-There')
#print(no4_a)
#print(no4_b)
#print(no4_c)

training = ('Whiskey')
#for num in training:
    #print(list(num*2))

#Question 5 
#Given 3 int values, abc, return their sum, However, if any of the values is #teen -- range of 13-19, then that value counts as 0, except
#15 and 16 do not count as a teen. Write a separate helper def fix_teen(n): that takes in an int value and returns that fixed value for the 
#teen rule.

#in this wat, you avoid repeating the teen code 3 times(i.e decomposition). 
#Define the helper below and at the same indent level as the nain no_teen_sum()
#Again you will have two functions for this problem!

#no_teen_sum(1,2,3) -> 6
#no_teen_sum(2,13,1) -> 3
#no_teen_sum(2,1,14) -> 3



def fix_teen(n):
     if n in [13,14,17,18,19]:
        return 0
     return n

def no_teen_sum(a,b,c):
     return fix_teen(a) + fix_teen(b) + fix_teen(c)

n5_a = no_teen_sum(1,2,3)
n5_b = no_teen_sum(2,13,1)
n5_c = no_teen_sum(2,1,14)
#Print(n5_a)
#Print(n5_b)
#Print(n5_c)

#Question 6
#Return the number of even integers in the given array
#count_Evens([2,1,2,3,4]) -> 3
#count_Evens([2,2,0]) -> 3
#count_Evens([1,3,5]) -> 0

#Solution
def count_evens(nums):
      entertainer = filter(lambda odd: odd%2 == 0,nums)
      return len(list(entertainer))


dreams1 = count_evens([2,1,2,3,4])
dreams2 = count_evens([2,2,0])
dreams3 = count_evens([1,3,5])
print(dreams1)
print(dreams2)
print(dreams3)