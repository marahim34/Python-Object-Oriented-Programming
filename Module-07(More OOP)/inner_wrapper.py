def double_in():
    print("Double in main function")

    def inner_in():
        print("Inside the inner function")
        return 3000

    return inner_in


print(double_in()())
