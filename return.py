def my_function(x):
    a = x + 5
    if a < 0:
        return "cannot be negative"
    else:
        return a

if __name__ == "__main__":
    i = -20
    answer = my_function(i)
    if answer is None:
        print("It returned nothing")
    else:
        print(answer)
