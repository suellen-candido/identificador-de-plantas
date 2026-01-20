from plantas import PlantaVascular, PlantaAvascular

class Briofita(PlantaAvascular):
    def exibir_classificacao(self):
        return f"{self.get_nome()} | Categoria: AVASCULAR (Briófita)"

class Pteridofita(PlantaVascular):
    def exibir_classificacao(self):
        return f"{self.get_nome()} | Categoria: VASCULAR -> SEM SEMENTE (Pteridófita)"

class Gimnosperma(PlantaVascular):
    def exibir_classificacao(self):
        return f"{self.get_nome()} | Categoria: VASCULAR -> COM SEMENTE -> SEM FRUTO (Gimnosperma)"

class Angiosperma(PlantaVascular):
    def exibir_classificacao(self):
        return f"{self.get_nome()} | Categoria: VASCULAR -> COM SEMENTE -> COM FRUTO (Angiosperma)"
