# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera
#É possivel incluir uma classe para os eventos - sorteando 
#       Os eventos podem ter diferentes probabilidades  

import random


class Evento:
    def __init__(self):
        self.numero = 0
        self.presente = 0
    
    def probabilidade(self):
        self.numero = random.randint(1,4) #excluí o evento em que ele não ganha ou perde dinheiro para facilitar a implementação do programa
        if self.numero == 1:
            print("Parabéns você ganhou na mega sena!!")
            premio = 1000000
            self.presente = premio
        elif self.numero == 2:
            print("Que sorte, você achou 50 reais!!")
            achado = 50
            self.presente = achado
        elif self.numero == 3:
            print("Os casos de violência aumentaram e você foi assaltado!!")
            self.presente = -50 
        elif self.numero == 4:
            print("Ja sabe da novidade? Devivo à sua alta produtividade a empresa resolveu te dar uma folga remunerada")
            self.presente = 100 
        


        

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False

class Casa:
    def __init__(self):
        self.remedios = 1
        self.comida = 5

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    evento_do_dia = Evento()
    cafe_da_manha = False
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Tomar remédio")
        print("6 - Comprar remédio")
        print("7 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            personagem.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                print("Não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            if(personagem.dinheiro >= 15):
                personagem.dinheiro -= 15
                cafe_da_manha = True
            else:
                print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
        elif(opcao == "4"):
            if(cafe_da_manha):
                personagem.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                print("Não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            if(casa.remedios > 0):
                casa.remedios -= 1
                personagem.medicado = True
            else:
                print("Não tem remédio na sua casa")
            relogio.avancaTempo(5)
        elif(opcao == "6"):
            if(personagem.dinheiro >= 20):
                casa.remedios += 10
                personagem.dinheiro -= 20
                relogio.avancaTempo(10)
            else:
                print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
        elif(opcao == "7"):
            print("-=-=-")
            print("Você foi trabalhar.")
            print(personagem)
            print("-=-=-")
            evento_do_dia.probabilidade()   #Fazendo o evento aleatório acontecer   
            if evento_do_dia.numero == 1:
                print("Você zerou o jogo!")
                break  #no caso de ganhar na mega sena, o jogador zera o jogo e ele acaba
            recebido = personagem.salario
            print("-=-=-")
            if(not personagem.medicado):
                print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
                recebido = 0
            elif(personagem.sujo):
                print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
                recebido *= 0.9
            elif(personagem.fome):
                print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
                recebido *= 0.5
            elif(relogio.atrasado()):
                print("Como você chegou atrasado, você produziu menos do que de costume.")
                recebido *= 0.8 
            
            recebido += evento_do_dia.presente #somando o dinheiro ganho ou perdido durante o evento aleatório
                         
            print("-=-=-")
            print("Você recebeu "+str(recebido)+" hoje.")
            print("-=-=-")

        
            
            personagem.dinheiro += recebido #se adiciona o recebido do dia ao dinheiro total do personagem
            personagem.dormir()
            relogio = Relogio()
            dia+=1
        elif(opcao == "0"):
            break
        else:
            print("Opção inválida!")
            Relogio.avancaTempo(5)