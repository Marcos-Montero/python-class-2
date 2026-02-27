# Crea una clase `Pokemon` con los atributos `name`, `type`, `hp` y `attack`.
# añade el método attack, quita hp al pokemon objetivo, en base a attack del pokemon atacante
# añade el método `faint`, que imprime un mensaje cuando el pokemon objetivo tiene 0 hp. (al finalizar el método attack llamaremos al target.faint())

class Pokemon:
    def __init__(self, name, type, hp, attack):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack

    def attack(self, target):
        target.hp -= self.attack
        print(f"{self.name} attacked {target.name} for {self.attack} damage")
        if target.hp <= 0:
            target.faint()

    def faint(self):
        if self.hp <= 0:
            print(f"{self.name} has fainted")


pikachu = Pokemon("Pikachu", "electric", 100, 50)
charizard = Pokemon("Charizard", "fire", 100, 50)

pikachu.attack(charizard)