def func1():
    pass

def func2():
    pass

class MyClass:
    def __init__(self):
        self.attribute = None

    def method1(self):
        pass

    def method2(self):
        pass

def main():
    my_var = 10
    another_var = "Hello"

    if my_var > 5:
        result = my_var + 5
    else:
        result = my_var - 5

    my_list = [1, 2, 3, 4, 5]
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    for item in my_list:
        if item % 2 == 0:
            print(item)
        else:
            continue

    for key, value in my_dict.items():
        if value > 1:
            break
        else:
            pass

if __name__ == "__main__":
    main()
