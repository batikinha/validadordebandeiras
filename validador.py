# Entrada do número do cartão
cartao = input("Digite o número do cartão: ").replace(" ", "")

# Função para identificar a bandeira
def identificar_bandeira(numero):
    # Verifica se o número tem apenas dígitos
    if not numero.isdigit():
        return "Número inválido (contém caracteres não numéricos)"

    # Verifica comprimento do cartão (comum: 13 a 16 dígitos)
    if len(numero) < 13 or len(numero) > 16:
        return "Número inválido (comprimento incorreto)"

    # Visa: começa com 4
    if numero.startswith("4"):
        return "Visa"

    # MasterCard: começa com 51 a 55 ou 2221 a 2720
    if 51 <= int(numero[:2]) <= 55 or 2221 <= int(numero[:4]) <= 2720:
        return "MasterCard"

    # American Express: começa com 34 ou 37
    if numero.startswith("34") or numero.startswith("37"):
        return "American Express"

    # Elo: faixas comuns (simplificadas)
    elo_prefixos = ["4011", "4312", "4389", "4514", "4576", "5041", "5067", "509", "6277", "6362", "650", "6516", "655"]
    if any(numero.startswith(prefixo) for prefixo in elo_prefixos):
        return "Elo"

    # Caso nenhuma condição seja satisfeita
    return "Bandeira não identificada"

# Chamada da função
bandeira = identificar_bandeira(cartao)

# Saída
print(f"Bandeira: {bandeira}")
