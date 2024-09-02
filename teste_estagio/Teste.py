def Ex1_Soma():
    indice = 13
    soma = 0
    k = 0

    while k < indice:
        k = k + 1
        soma = soma + k

    return soma


def Ex2_Fibonnaci(num):
    a, b = 0, 1

    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False

def Ex3_Faturamento(faturamento_diario):

    valores_faturamento = [valor for valor in faturamento_diario.values() if valor > 0]

    menor_faturamento = min(valores_faturamento)
    maior_faturamento = max(valores_faturamento)

    media_mensal = sum(valores_faturamento) / len(valores_faturamento)

    dias_acima_da_media = [dia for dia, valor in faturamento_diario.items() if valor > media_mensal]

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def Ex4_Percentual_Faturamento(faturamento_por_estado):
    faturamento_total = sum(faturamento_por_estado.values())

    percentual_por_estado = {}

    for estado, valor in faturamento_por_estado.items():
        percentual = (valor / faturamento_total) * 100
        percentual_por_estado[estado] = percentual

    return percentual_por_estado

def Ex5_Inverter_String(s):
    string_invertida = []
    
    for i in range(len(s) - 1, -1, -1):
        string_invertida.append(s[i])

    return string_invertida

def main():
    while True:
        print("\nMenu:")
        print("1. Somar os números de 1 até 13")
        print("2. Verificar se um número pertence à sequência de Fibonacci")
        print("3. Analisar faturamento mensal")
        print("4. Calcular percentual de faturamento por estado")
        print("5. Inverter uma string")
        print("6. Sair")
        
        escolha = input("Escolha uma opção (1-6): ")

        if escolha == '1':
            resultado = Ex1_Soma()
            print(f"Resultado da soma: {resultado}")

        elif escolha == '2':
            num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
            resultado = Ex2_Fibonnaci(num)
            if resultado:
                print(f"O número {num} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

        elif escolha == '3':
            faturamento_diario = {
                1: 2200, 2: 2100, 3: 2500, 4: 0, 5: 3000, 6: 2700, 7: 3400, 8: 3600,
                9: 0, 10: 3800, 11: 2900, 12: 0, 13: 2300, 14: 2100, 15: 3100, 16: 3000,
                17: 2600, 18: 0, 19: 4000, 20: 3500, 21: 3700, 22: 2900, 23: 0, 24: 2400,
                25: 3200, 26: 3300, 27: 0, 28: 4100, 29: 3800, 30: 2700
            }
            menor, maior, dias_acima_media = Ex3_Faturamento(faturamento_diario)
            print(f"Menor valor de faturamento: R$ {menor}")
            print(f"Maior valor de faturamento: R$ {maior}")
            print(f"Número de dias com faturamento superior à média mensal: {len(dias_acima_media)}")

        elif escolha == '4':
            faturamento_por_estado = {
                "SP": 67836.43,
                "RJ": 36678.66,
                "MG": 29229.88,
                "ES": 27165.48,
                "Outros": 19849.53
            }
            percentual_por_estado = Ex4_Percentual_Faturamento(faturamento_por_estado)
            print("Percentual de representação por estado:")
            for estado, percentual in percentual_por_estado.items():
                print(f"{estado}: {percentual:.2f}%")

        elif escolha == '5':

            s = input("Digite uma string para inverter: ")
            resultado = Ex5_Inverter_String(s)
            print(f"String invertida: {resultado}")

        elif escolha == '6':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")


if __name__ == "__main__":
    main()
