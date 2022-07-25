def fatorial(number: int) -> int:

    numero_fatorial = 1

    for i in range(1, number+1):
        numero_fatorial = i*numero_fatorial

    return numero_fatorial


if __name__ == "__main__":
    for number in range(0,7):
        print(fatorial(number))
