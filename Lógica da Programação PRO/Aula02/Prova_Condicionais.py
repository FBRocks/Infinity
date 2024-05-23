# Solicita a velocidade do carro ao usuário
velocidade_carro = float(input("Qual é a velocidade do seu carro em km/h? "))

# Verifica se a velocidade ultrapassa 80 km/h
if velocidade_carro > 80:
    # Calcula a quantidade de quilômetros que você ultrapassou o limite de velocidade
    km_excedidos = velocidade_carro - 80
    # Calcula o valor da multa
    valor_multa = km_excedidos * 20
    # Exibe uma mensagem informando que você foi multado e o valor da multa
    print("Você estava dirigindo acima do limite de velocidade permitido.")
    print("Você foi multado em R$ {:.2f} por exceder o limite de velocidade.".format(valor_multa))
else:
    # Se a velocidade não ultrapassar 80 km/h, exibe uma mensagem de que não houve multa
    print("Você está dentro do limite de velocidade. Não há multa.")
