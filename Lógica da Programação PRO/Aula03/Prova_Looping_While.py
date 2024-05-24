# Prova Looping While

# Inicializando as variáveis
quantidade_numeros = 0
soma = 0

# Loop para ler os números até que o usuário digite 0
while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    # Verifica se o número digitado é zero
    if numero == 0:
        break        
      
    # Incrementa a quantidade de números e adiciona o número à soma
    quantidade_numeros += 1
    soma += numero

# Verifica se foram digitados números antes de calcular a média
if quantidade_numeros > 0:
    media = soma / quantidade_numeros
else:
    media = 0

# Exibe a quantidade de números, a soma e a média
print("Quantidade de números digitados:", quantidade_numeros)
print("Soma dos números digitados:", soma)
print(f"Média dos números digitados: {media:.2f}")
