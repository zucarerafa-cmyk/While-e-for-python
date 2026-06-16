totalDePartidas = 0
totalDePontos = 0
melhorPontuação = 0

perguntas = [
   "1. Em que mês é comemorado a festa junina? ",
   "2. Em que mês é comemorado o natal? ",
   "3. Em que mês é comemorado a páscoa? ",
   "4. Em que mês é comemorado o halloween? ",
   "5. Em que mês é comemorado o dia das mães? ",
]
respostas = [
   "junho",
   "dezembro",
   "abril",
   "outubro",
   "maio",
]
jogarDnv = "Sim"

while jogarDnv.lower() == "sim":
    totalDePartidas = totalDePartidas + 1
    pontosDaPartida = 0

    for partida in range (5):
        print (perguntas[partida])
        respostaUsuário = input ("Digite a sua resposta: ").strip().lower()        

        if respostaUsuário == respostas[partida]:
            print ("Parabéns, você acertou (+1 ponto)")
            pontosDaPartida = pontosDaPartida + 1
        elif respostaUsuário != respostas[partida]:
            print ("Que pena, você errou.")
            print ("Resposta certa: ", respostas[partida])

    print ("Sua pontuação na partida foi: ", pontosDaPartida)

    totalDePontos = totalDePontos + pontosDaPartida
if pontosDaPartida > melhorPontuação:
   melhorPontuação = pontosDaPartida

   jogarDnv = input("Deseja jogar novamente? ")

   media = totalDePontos / totalDePartidas

print ("Fim de jogo")
print ("Total de partidas jogadas: ", totalDePartidas)
print ("Total de pontos gerais: ", totalDePontos)
print ("Melhor pontuação obtida: ", melhorPontuação)
print ("Média de pontos por partida: ", media)  
