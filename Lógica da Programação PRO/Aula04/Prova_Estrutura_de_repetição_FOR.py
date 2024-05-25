# Prova Estrutura de repetição: FOR

# Solicita ao usuário um número entre 1 e 10 para gerar a tabuada
numero = int(input("Digite um número entre 1 e 10 para gerar a tabuada: "))

# Verifica se o número fornecido está entre 1 e 10
if numero >= 1 and numero <= 10:
    
    # Indica qual número terá sua tabuada impressa
    print(f"Tabuada de {numero}:\n")
    
    # Loop for para gerar a tabuada
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    # Mostra um aviso se o número não estiver entre 1 e 10
    print("Por favor, digite um número entre 1 e 10.")