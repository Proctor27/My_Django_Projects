"""try:
    You do your operations here...
    ...
except ExceptionI:
    if there is ExceptionI, then execute this block.
except ExceptionII:
    if there is ExceptionII, then execute this block.
        ...
else:
    if there is no exception then execute this block.BlockingIOError"""

try:
    f = open('soledad.txt','r')
    #f.write("Asaim Alliaku")
except IOError:
        print("ERROR:Cound not find file or read data!")
else:
    print("Success!")
    f.close