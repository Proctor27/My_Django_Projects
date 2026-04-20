def func():
    print("func() in name.py")

print("Top level name.py")

if __name__ == '__main__':
    print('name.py is being run directly')
else:
    print('Name.py is being imported')