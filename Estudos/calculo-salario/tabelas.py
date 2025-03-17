FAIXAS_INSS = [
    (1518.00, 0.075, 0),  # Faixa 1: até R$ 1.518,00 - alíquota 7,5%
    (1275.87, 0.09, 22.77),  # Faixa 2: de R$ 1.518,01 até R$ 2.793,88 - alíquota 9%
    (1396.94, 0.12, 106.59),  # Faixa 3: de R$ 2.793,89 até R$ 4.190,83 - alíquota 12%
    (3966.57, 0.14, 190.40),  # Faixa 4: de R$ 4.190,84 até R$ 8.157,41 - alíquota 14%
    (float('inf'), 0.14, 0)   # Faixa 5: acima de R$ 8.157,42 - alíquota 14% sem dedução
]

# Faixas e deduções do IRRF (Atualizadas)
FAIXAS_IRRF = [
    (2259.20, 0, 0),  # Faixa 1: até R$ 2.259,20 - alíquota 0% e sem dedução
    (922.66, 0.075, 169.44),  # Faixa 2: de R$ 2.259,21 até R$ 2.828,65 - alíquota 7,5%
    (924.39, 0.15, 381.44),  # Faixa 3: de R$ 2.828,66 até R$ 3.751,05 - alíquota 15%
    (913.62, 0.225, 662.77),  # Faixa 4: de R$ 3.751,06 até R$ 4.664,68 - alíquota 22,5%
    (float('inf'), 0.275, 896.00)  # Faixa 5: acima de R$ 4.664,69 - alíquota 27,5%
]

# Teto atualizado do INSS
INSS_TETO = 961.64