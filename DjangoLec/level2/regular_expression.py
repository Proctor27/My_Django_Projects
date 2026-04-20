import re

"""all_i_ask = ["is if","this is my last night","it ends"]

adele = "It matters how it ends"

for honesty in all_i_ask:
    print("All i ask "+honesty)

    if re.search(honesty,adele):
        print("Match!")
    else:
        print("No mathch")"""

"""adele = "A million years ago"

match = re.search('million',adele)
print(type(match))"""

"""#split
melody = "@"

unchained = "tonycorp@gmail.com"

love = re.split(melody,unchained)
print(love)"""

#Multi refind
def unchained(patterns,phrase):
    for melody in patterns:
        print("Searching for patterns {}".format(melody))
        print(re.findall(melody,phrase))
        print('\n')

test_phrase = "Lonely! Time goes by? so slowly 2229943."
test_patterns = [r'\ +']

unchained(test_patterns,test_phrase)