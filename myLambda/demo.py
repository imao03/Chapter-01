class Demo:
    #
    totel = lambda a, b, c, d: a + b + c + d
    print(totel(1, 2, 3, 4))

    def test01(a, b, c, d):
        return a + b + c + d

    print(
        test01(1, 1, 1, 1)
    )

    g = [
        lambda a: a * 2,
        lambda b: b * 3
    ]

    print(g[1](1))
    print(type(g))


g = lambda x: x + 1


def g(x):
    return x + 1

