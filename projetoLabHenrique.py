

#criando variaveis e coletando informações
nomeAmostra = input("Informe nome da amostra:")
qtdTotal = float(input('Valor total:'))
qtdResiduo = float(input('Valor residuo (g):'))
qtdArdido = float(input('Valor ardido (g):'))
qtdCarunchado = float(input('Valor carunchado (g):'))
qtdQuebrado = float(input('Valor qubrado (g):'))
qtdOutrosAvariados = float(input('Valor outros avariados (g):'))
percentualUmidade = float(input('Valor umidade (%):'))

#calculando percentuais
percentualResiduo = (qtdResiduo * 100) / qtdTotal
percentualArdido = (qtdArdido * 100) / qtdTotal
percentualCarunchado = (qtdCarunchado * 100) / qtdTotal
percentualQuebrado = (qtdQuebrado * 100) / qtdTotal
percentualOutrosAvariados = (qtdOutrosAvariados * 100) / qtdTotal
percentualAvariadosTotais = percentualArdido + percentualCarunchado + percentualQuebrado + percentualOutrosAvariados

#exibindo percentuais
print(f'Percentual residuo: {percentualResiduo:.2f}% ')
print(f'Percentual ardido: {percentualArdido:.2f}% ')
print(f'Percentual carunchado: {percentualCarunchado:.2f}% ')
print(f'Percentual quebrado: {percentualQuebrado:.2f}% ')
print(f'Percentual outros avariados: {percentualOutrosAvariados:.2f}% ')
print(f'Percentual avariados totais: {percentualAvariadosTotais:.2f}% ')

#condição tipo1
#umidade < 14% e residuos <=1 andardidos <=1% e carunchados <= 2% e qubrados <= 3% e avariados total <= 6%
if percentualUmidade <= 14 and percentualResiduo <= 1 and percentualArdido <= 1 and percentualCarunchado <= 2 and percentualQuebrado <= 3 and percentualAvariadosTotais <= 6:
    print(f"A amostra {nomeAmostra} é do Tipo 1  ")

#condição tipo2
#umidade < 14% e residuos <= 1,5 ardidos and <=2% e carunchados <= 3% e qubrados <= 4% e avariados total <= 10%
elif percentualUmidade <= 14 and percentualResiduo <= 1.5 and percentualArdido <= 2 and percentualCarunchado <= 3 and percentualQuebrado <= 4 and percentualAvariadosTotais <= 10:
    print(f"A amostra {nomeAmostra} é do Tipo 2  ")

#condição tipo3
#umidade < 14% e residuos <= 2 ardidos <=3% e carunchados <= 4% e qubrados <= 5% e avariados total <= 15%
elif percentualUmidade <= 14 and percentualResiduo <= 2 and percentualArdido <= 3 and percentualCarunchado <= 4 and percentualQuebrado <= 5 and percentualAvariadosTotais <= 15:
    print(f"A amostra {nomeAmostra} é do Tipo 3  ")

else:
    print(f"A amostra {nomeAmostra} é Fora de Tipo")


