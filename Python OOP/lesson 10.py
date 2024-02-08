age = 1


def f1():
    age = 2

    def f2():
        nonlocal age
        age = 3

        def f3():
            nonlocal age
            age = 4
            print(age)

        f3()
        print(age)

    f2()
    print(age)


f1()
print(age)
