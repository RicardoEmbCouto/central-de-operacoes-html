# -*- coding: utf-8 -*-

def calcular_juros_compostos():
    """
    Função principal que calcula e exibe os resultados dos juros compostos.
    """
    print("="*40)
    print("  Calculadora de Juros Compostos - Couto Industries")
    print("="*40)
    print("Por favor, insira os dados abaixo.\n")

    try:
        # --- Coleta de Dados do Usuário ---
        valor_inicial = float(input("Valor Inicial (R$): "))
        aporte_mensal = float(input("Aporte Mensal (R$): "))
        taxa_juros_anual = float(input("Taxa de Juros Anual (%): "))
        periodo_anos = int(input("Período (em anos): "))

        # --- Cálculos ---
        taxa_juros_mensal = (taxa_juros_anual / 100) / 12
        total_meses = periodo_anos * 12
        
        valor_total = valor_inicial

        for mes in range(total_meses):
            # Adiciona o juro sobre o montante atual
            valor_total += valor_total * taxa_juros_mensal
            # Adiciona o novo aporte do mês
            valor_total += aporte_mensal
        
        total_investido = valor_inicial + (aporte_mensal * total_meses)
        total_juros = valor_total - total_investido

        # --- Apresentação dos Resultados ---
        print("\n" + "-"*40)
        print("                RESULTADO")
        print("-" * 40)
        print(f"Total Investido: R$ {total_investido:,.2f}")
        print(f"Total em Juros:  R$ {total_juros:,.2f}")
        print(f"Valor Total Acumulado: R$ {valor_total:,.2f}")
        print("-"*40)

    except ValueError:
        # Tratamento de erro caso o usuário digite algo que não seja um número.
        print("\n[ERRO] Por favor, insira apenas números válidos.")
    except Exception as e:
        # Tratamento para outros erros inesperados.
        print(f"\n[ERRO INESPERADO] Ocorreu um erro: {e}")

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    calcular_juros_compostos()


