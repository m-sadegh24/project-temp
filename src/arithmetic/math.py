def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(f"This modules name is {__name__}\nThe operator of 'add' and 'sub' is in that")
    assert add(3, 4) == 7
    print ("Done!")