def imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = (float(input("Digite seu peso: ")))
altura = (float(input("Digite sua altura: ")))

resultado = imc(peso, altura)
print(f"Seu IMC é de: {resultado:.2f}")
if resultado < 18.5:
    print("Abaixo do peso")
elif 18.5 <= resultado < 24.9:
    print("Peso normal")
elif 25 <= resultado < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
