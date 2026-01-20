from especies import Angiosperma


class IdentificadorBotanico:
    def __init__(self):
        self.banco = {
            "Comigo-ninguem-pode": "Extremamente toxica, usada para afastar mau-olhado.",
            "Pimenta Caiena": "Popular na culinaria, ja foi usada em flechas envenenadas.",
            "Espada-de-São-Jorge": "Ornamental e protetora, tambem conhecida como Espada-de-ogum.",
            "Mamão": "Fruto favorito do povo brasileiro, excelente para o intestino.",
            "Mandioca": "Raiz tuberosa com altissimo valor alimentar e cultural.",
            "Jiboia": "Trepadeira ornamental que se adaptou bem ao clima tropical.",
            "Rosa do deserto": "Suculenta escultural que pode demorar seculos para ser adulta."
        }

    def pergunta(self, texto):
        return input(f"{texto} (s/n): ").strip().lower() == 's'

    def identificar(self):
        print("\n--- IDENTIFICADOR DE PLANTAS: PENTECOSTE ---")

        vasos = self.pergunta("Possui sistema condutor (Xilema/Floema)?")
        sementes = self.pergunta("Produz sementes?")
        frutos = self.pergunta("Produz flores ou frutos?")

        if vasos and sementes and frutos:
            print("Escolha uma planta para detalhar: " + ", ".join(self.banco.keys()))
            nome = input("Digite o nome da planta: ")
            curiosidade = self.banco.get(nome, "Planta não encontrada no banco.")
            return Angiosperma(nome, curiosidade)

        return None

    def executar(self):
        planta = self.identificar()
        if planta:
            print("-=" * 30)
            print(f"RESULTADO: {planta.exibir_classificacao()}")
            print(f"CURIOSIDADE: {planta.get_curiosidade()}")
            print("-=" * 30)
        else:
            print("Não foi possivel classificar com os dados fornecidos.")


if __name__ == "__main__":
    app = IdentificadorBotanico()
    app.executar()