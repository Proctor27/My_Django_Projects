'''def sad_girl(param1 = 'lana'):
    """
    ddddddddd
    ddddddddddd 
    docstring
    ddddddddd
    """

    print('nothing{}'.format(param1))
sad_girl()



def hello():
    return "nothing"
result = hello()
print(result)


def Addition(x,y):
    if x == y == type(10):
        return x + y
    else:
        return "Give me integers"
result = Addition(2,'barbie')
print(result)
                '''

# lambda
#a function used one time   lambda Expression used in a function that accepts another function like the filter function

#FIlter Function
#filter takes two arguments, a function and a sequence
listed = [1,2,3,4,5,6,7,8,9,19]
def even_numbers(even_number):
    return even_number%2 != 0 
even =filter(even_numbers,listed)
print(list(even))

#lambda Expression
entertainer = filter(lambda odd: odd%2 != 0,listed)
print(list(entertainer))


#split Method
#In method