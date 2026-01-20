from especies import Angiosperma, Pteridofita, Gimnosperma, Briofita


class IdentificadorBotanico:
    def __init__(self):
        self.banco_briofitas = {
            "Musgo": "Planta de pequeno porte que vive em ambientes úmidos e sombreados, encontrada em áreas mais frescas de Pentecoste."
        }

        self.banco_pteridofitas = {
            "Samambaia": "Planta ornamental que cresce em áreas com mais umidade, possui folhas compostas chamadas frondes.",
            "Avenca": "Samambaia delicada com folhas pequenas, encontrada em locais úmidos da região."
        }

        self.banco_gimnospermas = {
            "Pinhão-bravo": "Planta xerófita adaptada ao clima semiárido, encontrada ocasionalmente na região.",
            "Rosa do deserto": "Suculenta escultural com flores vistosas, adaptada ao clima seco."
        }

        self.banco_angiospermas = {
            "Mamão": "Fruto favorito do povo brasileiro, excelente para o intestino.",
            "Mandioca": "Raiz tuberosa com altíssimo valor alimentar e cultural.",
            "Jiboia": "Trepadeira ornamental que se adaptou bem ao clima tropical.",
            "Espada-de-São-Jorge": "Ornamental e protetora, também conhecida como Espada-de-ogum.",
            "Marmeleiro": "Arbusto da Caatinga que perde folhas na seca, possui frutos comestíveis.",
            "Aroeira": "Árvore resistente da Caatinga, madeira nobre usada para lenha e construção.",
            "Caatingueira": "Arbusto típico que dá nome à Caatinga, muito resistente à seca."
        }

    def pergunta(self, texto):
        return input(f"{texto} \n(s/n): ").strip().lower() == 's'

    def selecionar_planta(self, categorias_disponiveis):
        print("Plantas correspondentes: " + ", ".join(categorias_disponiveis.keys()))
        print('-='*30)
        nome = input("Digite o nome da planta que você quer ver mais informações: ")
        curiosidade = categorias_disponiveis.get(nome)

        if not curiosidade:
            print("Erro: Esta planta não condiz com as características informadas ou não está no banco.")
            return None, None
        return nome, curiosidade

    def identificar(self):
        print("--- Identificação e Classificação de Plantas presentes na Flora Pentecostense ---")

        vasos = self.pergunta("Possui sistema condutor (Xilema/Floema)? ")

        sementes = None
        frutos = None

        if vasos:
            sementes = self.pergunta("Produz sementes? ")
            if sementes:
                frutos = self.pergunta("Produz flores ou frutos? ")

        if not vasos:
            categorias_disponiveis = self.banco_briofitas
            tipo_planta = "Briófita"
        elif not sementes:
            categorias_disponiveis = self.banco_pteridofitas
            tipo_planta = "Pteridófita"
        elif not frutos:
            categorias_disponiveis = self.banco_gimnospermas
            tipo_planta = "Gimnosperma"
        else:
            categorias_disponiveis = self.banco_angiospermas
            tipo_planta = "Angiosperma"

        nome, curiosidade = self.selecionar_planta(categorias_disponiveis)
        if not nome:
            return None

        if not vasos:
            return Briofita(nome, curiosidade)
        elif not sementes:
            return Pteridofita(nome, curiosidade)
        elif not frutos:
            return Gimnosperma(nome, curiosidade)
        else:
            return Angiosperma(nome, curiosidade)

    def executar(self):
        planta = self.identificar()
        if planta:
            print("=-" * 30)
            print(f"RESULTADO: {planta.exibir_classificacao()}")
            print(f"CURIOSIDADE: {planta.get_curiosidade()}")
            print("=-" * 30)


if __name__ == "__main__":
    app = IdentificadorBotanico()
    app.executar()
