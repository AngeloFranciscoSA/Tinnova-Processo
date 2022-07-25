def soma_multiplos(number: int) -> int:

    n = 0

    for i in range(1,number):
        if not i % 5 or not i % 3:
            n = n + i

    return n


if __name__ == "__main__":

    print(soma_multiplos(10))