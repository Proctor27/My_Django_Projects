##QUESTION 1
s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
#reverse = s.reverse()
o = s[-1]
g =s[-2]
n =s[-3]
a =s[-4]
j= s[-5]
d = s[-6]
man = o + g + n + a + j + d
print(man)
#use step
print(s[::-1])

#QUESTION 2 Turn hello to goodbye
L = [3,7,[1,4,'Hello']]
L[-1][-1] = 'goodbye'
print(L)

#Question 3 Grab hello
d1 = {'simply_key': 'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'K1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simply_key'])
print(d2['k1']['k2'])
print(d3['K1'][0]['nest_key'][1][0])

v = {'nest_key':['this is deep',['hello']]}
print(v['nest_key'][1][0])

#Problem 4 USe set to find the unique values
mylist = [1,1,1,1,2,2,2,2,3,3,3,3]
blue = set(mylist)
print(blue)

#Problem 5 Print formatting
age = 4
name = "Sammy"

Black = "Hello my dog's name is {w} and he is {s} years old".format(w=name, s = age)
print(Black)