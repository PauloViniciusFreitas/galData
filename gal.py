import pandas as pd
from pandas._config.config import Display


def line():
    print('-'*148)


# Carrega a planilha (substitua 'caminho_para_sua_planilha.csv' pelo caminho real)
df = pd.read_csv('IES_Página1.csv')

# Conta a frequência de cada valor na coluna "Horário de exposição solar"
contagem_a = df['Sexo'].value_counts()
contagem_b = df['Ocupação'].value_counts()
contagem_c = df['Horário de exposição solar'].value_counts()
contagem_d = df['Tempo de exposição'].value_counts()
contagem_e = df['Motivo de exposição '].value_counts()
contagem_f = df['Bronzeamento'].value_counts()
contagem_g = df['Uso de protetor'].value_counts()
contagem_h = df['Reaplicação'].value_counts()
contagem_i = df['Reaplicação'].value_counts()
contagem_j = df['conhecimento sobre doenças de pele '].value_counts()
contagem_k = df['afecções de pele que conhece'].value_counts()
# Calcula a porcentagem de cada valor, arredondando para uma casa decimal
porcentagem_a = (contagem_a / contagem_a.sum() * 100).round(1)
porcentagem_b = (contagem_b / contagem_b.sum() * 100).round(1)
porcentagem_c = (contagem_c / contagem_c.sum() * 100).round(1)
porcentagem_d = (contagem_d / contagem_d.sum() * 100).round(1)
porcentagem_e = (contagem_e / contagem_e.sum() * 100).round(1)
porcentagem_f = (contagem_f / contagem_f.sum() * 100).round(1)
porcentagem_g = (contagem_g / contagem_g.sum() * 100).round(1)
porcentagem_h = (contagem_h / contagem_h.sum() * 100).round(1)
porcentagem_i = (contagem_i / contagem_i.sum() * 100).round(1)
porcentagem_j = (contagem_j / contagem_j.sum() * 100).round(1)
porcentagem_k = (contagem_k / contagem_k.sum() * 100).round(1)


# Cria um DataFrame com as informações
tabela_a = pd.DataFrame({
    'Horário de Exposição Solar': ['Masculino (1)', 'Feminino (2)'],
    'Número de Ocorrências (n)': [
        contagem_h.get(1, 0),
        contagem_h.get(2, 0),

    ],
    'Porcentagem (%)': [
        porcentagem_a.get(1, 0),
        porcentagem_a.get(2, 0),

    ]
})

tabela_b = pd.DataFrame({
    'Ocupação': ['trabalha em local coberto (1)', 'trabalha em local exposto ao sol (2)', 'não trabalha (3)'],
    'Número de Ocorrências (n)': [
        contagem_b.get(1, 0),
        contagem_b.get(2, 0),
        contagem_b.get(3, 0)
    ],
    'Porcentagem (%)': [
        porcentagem_b.get(1, 0),
        porcentagem_b.get(2, 0),
        porcentagem_b.get(2, 0)
    ]
})

tabela_c = pd.DataFrame({
    'Horário de Exposição Solar': ['Manhã (1)', 'Tarde (2)', 'Manhã e Tarde (3)', 'Não se expõe (4)'],
    'Número de Ocorrências (n)': [
        contagem_c.get(1, 0),
        contagem_c.get(2, 0),
        contagem_c.get(3, 0),
        contagem_c.get(4, 0)
    ],
    'Porcentagem (%)': [
        porcentagem_c.get(1, 0),
        porcentagem_c.get(2, 0),
        porcentagem_c.get(3, 0),
        porcentagem_c.get(4, 0)
    ]
})

tabela_d = pd.DataFrame({
    'Tempo de exposição': ['até 2h (1)', '2h-6h (2)', 'mais de 6h (3)', 'não se expõe (4)'],
    'Número de Ocorrências (n)': [
        contagem_d.get(1, 0),
        contagem_d.get(2, 0),
        contagem_d.get(3, 0),
        contagem_d.get(4, 0)
    ],
    'Porcentagem (%)': [
        porcentagem_d.get(1, 0),
        porcentagem_d.get(2, 0),
        porcentagem_d.get(3, 0),
        porcentagem_d.get(4, 0)
    ]
})

tabela_e = pd.DataFrame({
    'Motivo da exposição': ['deslocamento (1)', 'trabalho sob exposição (2)', 'lazer (3)', 'exercício físico (4)', 'trabalho e deslocamento (5)', 'não se expõe (6)'],
    'Número de Ocorrências (n)': [
        contagem_e.get(1, 0),
        contagem_e.get(2, 0),
        contagem_e.get(3, 0),
        contagem_e.get(4, 0),
        contagem_e.get(5, 0),
        contagem_e.get(6, 0)
    ],
    'Porcentagem (%)': [
        porcentagem_e.get(1, 0),
        porcentagem_e.get(2, 0),
        porcentagem_e.get(3, 0),
        porcentagem_e.get(4, 0),
        porcentagem_e.get(5, 0),
        porcentagem_e.get(6, 0)
    ]
})
tabela_f = pd.DataFrame({
    'Bronzeamento': ['Nunca (1)', 'As vezes (2)', 'Sempre (3)'],
    'Número de Ocorrências (n)': [
        contagem_f.get(1, 0),
        contagem_f.get(2, 0),
        contagem_f.get(3, 0),

    ],
    'Porcentagem (%)': [
        porcentagem_f.get(1, 0),
        porcentagem_f.get(2, 0),
        porcentagem_f.get(3, 0),

    ]
})

tabela_g = pd.DataFrame({
    'Uso de protetor': ['Nunca (1)', 'As vezes (2)', 'Sempre (3)'],
    'Número de Ocorrências (n)': [
        contagem_g.get(1, 0),
        contagem_g.get(2, 0),
        contagem_g.get(3, 0),

    ],
    'Porcentagem (%)': [
        porcentagem_g.get(1, 0),
        porcentagem_g.get(2, 0),
        porcentagem_g.get(3, 0),

    ]
})

tabela_h = pd.DataFrame({
    'Reaplicação': ['1-3 vezes (1)', 'mais de 3 vezes (2)', 'não reaplica (3)', 'não faz uso (4)'],
    'Número de Ocorrências (n)': [
        contagem_h.get(1, 0),
        contagem_h.get(2, 0),
        contagem_h.get(3, 0),
        contagem_h.get(4, 0),
    ],
    'Porcentagem (%)': [
        porcentagem_h.get(1, 0),
        porcentagem_h.get(2, 0),
        porcentagem_h.get(3, 0),
        porcentagem_h.get(4, 0),
    ]
})
tabela_i = pd.DataFrame({
    'Barreiras': ['Uma (1)', 'Duas a três (2)', 'Mais de três (3)', 'Nenhuma (4)'],
    'Número de Ocorrências (n)': [
        contagem_i.get(1, 0),
        contagem_i.get(2, 0),
        contagem_i.get(3, 0),
        contagem_i.get(4, 0),
    ],
    'Porcentagem (%)': [
        porcentagem_i.get(1, 0),
        porcentagem_i.get(2, 0),
        porcentagem_i.get(3, 0),
        porcentagem_i.get(4, 0),
    ]
})

tabela_j = pd.DataFrame({
    'conhecimento sobre doenças de pele': ['Sim (1)', 'Não (2)'],
    'Número de Ocorrências (n)': [
        contagem_j.get(1, 0),
        contagem_j.get(2, 0),
    ],
    'Porcentagem (%)': [
        porcentagem_j.get(1, 0),
        porcentagem_j.get(2, 0),
    ]
})
tabela_k = pd.DataFrame({
    'Afecções de pele que conhece': ['Uma (1)', 'Duas a três (2)', 'Mais de três (3)', 'Não conhece (4)'],
    'Número de Ocorrências (n)': [
        contagem_k.get(1, 0),
        contagem_k.get(2, 0),
        contagem_k.get(3, 0),
        contagem_k.get(4, 0),
    ],
    'Porcentagem (%)': [
        porcentagem_k.get(1, 0),
        porcentagem_k.get(2, 0),
        porcentagem_k.get(3, 0),
        porcentagem_k.get(4, 0),
    ]
})

# Exibe a tabela
Display(tabela_a)
line()
print(tabela_b)
line()
print(tabela_c)
line()
print(tabela_d)
line()
print(tabela_e)
line()
print(tabela_f)
line()
print(tabela_g)
line()
print(tabela_h)
line()
print(tabela_i)
line()
print(tabela_j)
line()
print(tabela_k)
