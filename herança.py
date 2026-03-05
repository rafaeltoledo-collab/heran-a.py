class Animal():
    def __init__(self, nome, cor, raça):
        self.__nome = nome
        self.__cor = cor 
        self.__raça = raça


    def comer(self):    
        print(f"O {self.__nome} está comendo!") 
        
    def raça(self):
       print(f"E sua raça é:{self.__raça}")

class gato(Animal): 
    def __init__(self, nome, cor, raça):
     super().__init__(nome, cor, raça)
    

class cachorro(Animal):
    def __init__(self, nome, cor, raça):
     super().__init__(nome, cor, raça)
    

class coelho(Animal):
    def __init__(self, nome, cor, raça):
     super().__init__(nome, cor, raça)


ramona = gato("ramona", "preto", "siames")
ramona.comer()
ramona.raça()

chocolate = gato("chocolate", "roxo", "persa")
chocolate.comer()
chocolate.raça()

tobi = cachorro("tobi", "caramelo", "viralata")
tobi.comer()
tobi.raça()

maya = cachorro("maya", "preto", "rottweiler")
maya.comer()
maya.raça()