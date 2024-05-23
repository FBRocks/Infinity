# Prova Algoritmos e Variáveis

# Principais tipagens de variáveis

# 1. Inteiro (int)
idade = 25

# 2. Ponto flutuante (float)
altura = 1.75

# 3. String (str)
nome = "João"

# 4. Booleano (bool)
e_estudante = True

# Solicitação de dados ao usuário
nome_usuario = input("Por favor, digite seu nome: ")
idade_usuario = int(input("Por favor, digite sua idade: "))
altura_usuario = float(input("Por favor, digite sua altura (em metros): "))
e_estudante_usuario = input("Você é estudante? (sim/não): ").lower() == 'sim'

# Imprimir os dados com uma mensagem personalizada
print(f"\nBem-vindo, {nome_usuario}!")
print(f"Você tem {idade_usuario} anos e mede {altura_usuario:.2f} metros.")
if e_estudante_usuario:
    print("Que bom saber que você é um estudante!")
else:
    print("Você não é um estudante!")