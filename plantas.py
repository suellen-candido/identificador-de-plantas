class Planta:
    def __init__(self, nome, curiosidade):
        self.__nome = nome
        self.__curiosidade = curiosidade

    def get_nome(self):
        return self.__nome

    def get_curiosidade(self):
        return self.__curiosidade

    def exibir_classificacao(self):
        raise NotImplementedError("Subclasses devem implementar este metodo!")

class PlantaVascular(Planta):
    def __init__(self, nome, curiosidade):
        super().__init__(nome, curiosidade)