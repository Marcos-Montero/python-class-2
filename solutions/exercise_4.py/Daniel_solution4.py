# Crea una clase `Pokemon` con los atributos `name`, `type`, `hp` y `attack`.
# añade el método attack, quita hp al pokemon objetivo, en base a attack del pokemon atacante
# añade el método `faint`, que imprime un mensaje cuando el pokemon objetivo tiene 0 hp. (al finalizar el método attack llamaremos al target.faint())

class Pokemon:
    def __init__(self, name, type, hp, attack_power):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage")

        # comprobar si el objetivo se ha debilitado
        target.faint()

    def faint(self):
        if self.hp <= 0:
            print(f"{self.name} has fainted")


pikachu = Pokemon("Pikachu", "electric", 100, 50)
charizard = Pokemon("Charizard", "fire", 100, 50)

pikachu.attack(charizard)
charizard.attack(pikachu)