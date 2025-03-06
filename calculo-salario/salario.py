from tabelas import FAIXAS_INSS, FAIXAS_IRRF, DEDUCOES_IRRF

def calcular_salario_liquido(salario_bruto, beneficios=0, outros_descontos=0):
    """
    Calcula o salário líquido considerando INSS, IRRF, benefícios e outros descontos.
    """
    # Cálculo do INSS
    inss = 0
    salario_restante = salario_bruto
    for limite, aliquota in FAIXAS_INSS:
        if salario_restante > limite:
            inss += limite * aliquota
            salario_restante -= limite
        else:
            inss += salario_restante * aliquota
            break
    inss = min(inss, 961.64)  # Teto do INSS
    
    # Base de cálculo do IRRF
    base_irrf = salario_bruto - inss
    
    # Cálculo do IRRF
    irrf = 0
    salario_restante = base_irrf
    for i, (limite, aliquota) in enumerate(FAIXAS_IRRF):
        if salario_restante > limite:
            irrf += (limite - (FAIXAS_IRRF[i-1][0] if i > 0 else 0)) * aliquota
        else:
            irrf += (salario_restante - (FAIXAS_IRRF[i-1][0] if i > 0 else 0)) * aliquota
            break
    irrf -= DEDUCOES_IRRF[i]  # Aplicando dedução
    irrf = max(irrf, 0)  # IRRF não pode ser negativo
    
    # Salário líquido
    salario_liquido = salario_bruto - inss - irrf + beneficios - outros_descontos
    
    return {
        "Salário Bruto": salario_bruto,
        "INSS": round(inss, 2),
        "IRRF": round(irrf, 2),
        "Benefícios": beneficios,
        "Outros Descontos": outros_descontos,
        "Salário Líquido": round(salario_liquido, 2)
    }

# Entrada do usuário
salario_bruto = float(input("Digite o salário bruto: "))
beneficios = float(input("Digite o valor dos benefícios: "))
outros_descontos = float(input("Digite o valor de outros descontos: "))

# Cálculo e exibição do resultado
salario = calcular_salario_liquido(salario_bruto, beneficios, outros_descontos)
for chave, valor in salario.items():
    print(f"{chave}: R$ {valor}")