# Perguntas e respostas em dicionários. Treino de dicionários
dicioPerguntas = {
        1: {
            'Pergunta':'Quem eram os apóstolos mais chegados?',
            'Respostas':{'a':'Pedro, Tiago e João', 'b':'Mateus, Marcos e Lucas', 'c':'Marcos, Judas, Thomé', 'd':'Silas, Paulo, Timóteo', 'e':'Lucas e Zaqueu'},
            'Resposta_certa': 'a',
    },
        2: {
            'Pergunta':'Quem escreveu os evangelhos Sinóticos',
            'Respostas':{'a':'Pedro, Tiago e João', 'b':'Mateus, Marcos e Lucas', 'c':'Marcos, Judas, Thomé', 'd':'Silas, Paulo, Timóteo', 'e':'Lucas e Zaqueu'},
            'Resposta_certa': 'b',
    },
        3: {
            'Pergunta':'Qual nome do apóstolo que substituiu Judas Iscariotes?',
            'Respostas':{'a':'Paulo', 'b':'Silas', 'c':'Matias', 'd':'Timóteo', 'e':'Zaqueu'},
            'Resposta_certa': 'b',
    }
}

print()

respostasCertas = 0

for perguntaKeys, perguntaValues in dicioPerguntas.items(): # O .items() designa todos os itens do dicionario
    print(f'{perguntaKeys}:{perguntaValues["Pergunta"]}')

    print('Respostas: ')

    for respostaKeys, respostaValues in perguntaValues['Respostas'].items():
        print(f'[{respostaKeys}]: {respostaValues}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == perguntaValues['Resposta_certa']:
        print('Ótimo, você acertou, Parabéns!!!!')
        respostasCertas += 1
    else:
        print('Puxa, vc errou. Tem que ir mais na EBD!!!!')

    print()

quantidadePerguntas = len(dicioPerguntas)
porcentagemAcerto = respostasCertas / quantidadePerguntas * 100
print(f'Você respondeu corretamente {respostasCertas} perguntas.')
print(f'Sua porcentagem de acerto foi {porcentagemAcerto:.2f}%.')

if porcentagemAcerto == 100:
    print("Parabéns, você parece ser um obreiro aprovado!!! Continue assim!!!")
elif porcentagemAcerto >= 75:
    print("Seu desempenho foi bom. Leia mais a Bíblia para melhorar!")
elif porcentagemAcerto >= 50:
    print("Sua situação está meio complicada. Acorde cedo domingo de manhã e vá para EBD!")
else:
    print("Misericórdia, se você ler a Bíblia 30 minutos por dia e ir na EBD todos os domingos você melhora!")