# Sistema de Classificação e Identificação de Plantas . ˚ ⸙  ୭ ˚. 

Este sistema foi desenvolvido como projeto final da disciplina de Programação Orientada a Objetos (POO). O objetivo é facilitar a identificação e classificação científica de plantas representativas da região de Pentecoste (CE), utilizando uma interface interativa baseada em chaves dicotômicas.

O software utiliza categorias padronizadas pela comunidade científica (Vascualares, Avasculares, Angiospermas, etc.) para catalogar espécies locais como a Mandioca, Pimenta Caiena e a Espada-de-São-Jorge.

## O que o Sistema de Classificação de Identificação de Plantas faz?
É uma ferramenta botânica que utiliza uma sequência de perguntas binárias (Sim/Não) para classificar organismos.

- Processo de Identificação Interativa: O programa guia o usuário através das ramificações do reino vegetal contidas no Anexo 1 do projeto, perguntando sobre a presença de vasos condutores, sementes e frutos.

- Classificação Científica: Com base nas respostas, o software instancia objetos de classes específicas (como Angiosperma ou Pteridofita), aplicando automaticamente a taxonomia correta.

- Consulta ao Banco de Dados Regional: Após a classificação técnica, o usuário pode consultar informações detalhadas sobre as plantas comuns em Pentecoste, como a Comigo-ninguém-pode, o Mamão e a Mandioca.

- Educação e Segurança: Além da classificação botânica, o programa exibe curiosidades e alertas importantes sobre a flora local, como os riscos de toxicidade da Espada-de-São-Jorge e da Zamioculcas ou as propriedades nutricionais da Beldroega.

## Pilares de POO Implementados:
Para atender aos requisitos solicitados, o sistema contempla:

- Abstração: Uso de classes base que definem comportamentos essenciais para todas as plantas.

- Encapsulamento: Proteção de dados sensíveis (nomes e curiosidades) através de atributos privados e métodos de acesso.

- Herança: Organização hierárquica onde subclasses herdam características de classes superiores (ex: Angiosperma herda de PlantaVascular).

- Polimorfismo: O método exibir_classificacao() comporta-se de forma específica para cada tipo de planta identificada.

## Estrutura de Arquivos
O projeto está organizado em módulos para garantir a escalabilidade:

- plantas.py: Contém a lógica das classes base e intermediárias.

- especies.py: Contém as definições das categorias finais de plantas.

- main.py: Arquivo principal que executa o sistema de perguntas e a interface com o usuário.

## Diagrama UML
<img width="891" height="647" alt="image" src="https://github.com/user-attachments/assets/b7fe14fd-afc1-4962-8344-1967b7715b53" />



## Doa
