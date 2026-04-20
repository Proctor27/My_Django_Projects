import name
print("top level main.py")
name.func()

if __name__ == '__main__':
    print("main,py is being imported")
else:
    print("main.py is being imported")