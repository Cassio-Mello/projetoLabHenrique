from PySimpleGUI import PySimpleGUI as sg

sg.theme('Dark Blue 3')
layout = [
    [sg.Text('Data:'), sg.Input(key='data', size=(10, 1)), sg.Text('Nome Amostra:'), sg.Input(key='nomeAmostra', size=(15, 1))],
    #[sg.Text('Nome Amostra:'), sg.Input(key='nomeAmostra', size=(10, 1)),
    [sg.Text('Fornecedor:'), sg.Input(key='nomeFornecedor', size=(30, 1))],
    [sg.Text('Valor Total (g):'), sg.Input(key='valorTotal', size=(10, 1))],
    [sg.Text('Valor Residuos (g):'), sg.Input(key='valorResiduos', size=(10, 1))],
    [sg.Text('Valor Ardidos (g)'), sg.Input(key='valorArdidos', size=(10, 1))],
    [sg.Text('Valor Carunchados (g):'), sg.Input(key='valorCarunchados', size=(10, 1))],
    [sg.Text('Valor Quebrados (g):'), sg.Input(key='valorQuebrados', size=(10, 1))],
    [sg.Text('Valor Outros Avariados (g):'), sg.Input(key='valorOutrosAvariados', size=(10, 1))],
    [sg.Text('Valor Umidade (%):'), sg.Input(key='valorUmidade', size=(10, 1))],
    [sg.Button('Calcular')]
    
]
#janela
janela = sg.Window('Calculo IMC', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Calcular':
        percentualResiduo = (float(valores['valorResiduos']) * 100) / valores['valorTotal']
        percentualArdido = (float(valores['ValorArdidos']) * 100) / valores['valorTotal']
        percentualCarunchado = (float(valores['valorCarunchados']) * 100) / valores['valorTotal']
        percentualQuebrado = (float(valores['valorQuebrados']) * 100) / valores['valorTotal']
        percentualOutrosAvariados = (float(valores['valorOutrosAvariados']) * 100) / valores['valorTotal']
        percentualAvariadosTotais = percentualArdido + percentualCarunchado + percentualQuebrado + percentualOutrosAvariados
        percentualUmidade = float(valores['valorUmidade'])
    #condição tipo1
    #umidade < 14% e residuos <=1 andardidos <=1% e carunchados <= 2% e qubrados <= 3% e avariados total <= 6%
    if percentualUmidade <= 14 and percentualResiduo <= 1 and percentualArdido <= 1 and percentualCarunchado <= 2 and percentualQuebrado <= 3 and percentualAvariadosTotais <= 6:
        rint(f"A amostra {nomeAmostra} é do Tipo 1  ")

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