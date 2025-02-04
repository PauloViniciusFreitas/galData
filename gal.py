import pandas as pd

# Função para traçar a linha separadora


def line():
    print('-' * 148)

# Função para gerar a tabela com base na coluna e descrição


def gerar_tabela(nome_coluna, descricao_valores):
    contagem = df[nome_coluna].value_counts()
    porcentagem = (contagem / contagem.sum() * 100).round(1)

    # Cria o DataFrame com as descrições e valores
    tabela = pd.DataFrame({
        'Categoria': descricao_valores,
        'Número de Ocorrências (n)': [contagem.get(i, 0) for i in range(1, len(descricao_valores) + 1)],
        'Porcentagem (%)': [porcentagem.get(i, 0) for i in range(1, len(descricao_valores) + 1)]
    })

    return tabela


# Carrega a planilha
df = pd.read_csv('/home/vinnie/github-repos/galData/data.csv')

# Dicionário para mapeamento das colunas e suas descrições
tabelas_info = {
    'Sexo': ['Masculino (1)', 'Feminino (2)'],
    'Ocupação': ['trabalha em local coberto (1)', 'trabalha em local exposto ao sol (2)', 'não trabalha (3)'],
    'Horário de exposição solar': ['Manhã (1)', 'Tarde (2)', 'Manhã e Tarde (3)', 'Não se expõe (4)'],
    'Tempo de exposição': ['até 2h (1)', '2h-6h (2)', 'mais de 6h (3)', 'não se expõe (4)'],
    'Motivo de exposição ': ['deslocamento (1)', 'trabalho sob exposição (2)', 'lazer (3)', 'exercício físico (4)', 'trabalho e deslocamento (5)', 'não se expõe (6)'],
    'Bronzeamento': ['Nunca (1)', 'As vezes (2)', 'Sempre (3)'],
    'Uso de protetor': ['Nunca (1)', 'As vezes (2)', 'Sempre (3)'],
    'Reaplicação': ['1-3 vezes (1)', 'mais de 3 vezes (2)', 'não reaplica (3)', 'não faz uso (4)'],
    'conhecimento sobre doenças de pele ': ['Sim (1)', 'Não (2)'],
    'afecções de pele que conhece': ['Uma (1)', 'Duas a três (2)', 'Mais de três (3)', 'Não conhece (4)']
}

# Geração e exibição das tabelas
for coluna, descricoes in tabelas_info.items():
    tabela = gerar_tabela(coluna, descricoes)
    print(f"Tabela: {coluna}")
    print(tabela)
    line()

    # hello world
