class Eleitores:

    def __init__(self, total_eleitores: int, votos_validos: int, votos_brancos : int, votos_nulos : int):
        self.__total_eleitores = total_eleitores
        self.__votos_validos = votos_validos
        self.__votos_brancos = votos_brancos
        self.__votos_nulos = votos_nulos

    def cal_votos_validos(self) -> str:
        return f"{str(self.__votos_validos/self.__total_eleitores * 100)}%"

    def cal_votos_brancos(self) -> str:
        return f"{str(self.__votos_brancos / self.__total_eleitores * 100)}%"

    def cal_votos_nulos(self) -> str:
        return f"{str(self.__votos_nulos / self.__total_eleitores * 100)}%"