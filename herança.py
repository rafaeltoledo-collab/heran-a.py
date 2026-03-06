class Animal():
    def __init__(self, nome, cor, raça):
        self.__nome = nome
        self.__cor = cor 
        self.__raca = raca


    def comer(self):    
        print(f"O {self.__nome} está comendo!") 
        
    def raça(self):
       print(f"E sua raca é:{self.__raca}")

class gato(Animal): 
    def __init__(self, nome, cor, raca):
     super().__init__(nome, cor, raca)
    

class cachorro(Animal):
    def __init__(self, nome, cor, raca):
     super().__init__(nome, cor, raca)
    

class coelho(Animal):
    def __init__(self, nome, cor, raca):
     super().__init__(nome, cor, raca)


ramona = gato("ramona", "preto", "siames")
ramona.comer()
ramona.raca()

chocolate = gato("chocolate", "roxo", "persa")
chocolate.comer()
chocolate.raca()

tobi = cachorro("tobi", "caramelo", "viralata")
tobi.comer()
tobi.raca()

maya = cachorro("maya", "preto", "rottweiler")
maya.comer()
maya.raca()
