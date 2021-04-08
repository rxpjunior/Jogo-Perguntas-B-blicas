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

for perguntaKeys, perguntaValues in dicioPerguntas.items(): # O .items() designa todos os itens do dicionario
    print(perguntaKeys, ' : ', perguntaValues)              # As chaves e valores, imprimindo tudo
    print()