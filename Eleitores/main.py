from Eleitores import Eleitores

def main():
    eleitores = Eleitores(total_eleitores = 1000, votos_validos = 800,votos_brancos = 150, votos_nulos = 50)
    print(eleitores.cal_votos_validos())
    print(eleitores.cal_votos_brancos())
    print(eleitores.cal_votos_nulos())

if __name__ == "__main__":
    main()