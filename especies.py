from plantas import PlantaVascular

class Angiosperma(PlantaVascular):
    def exibir_classificacao(self):
        return f"{self.get_nome()} | Categoria: VASCULAR -> COM SEMENTE -> COM FRUTO (Angiosperma)"
