# Crea una clase `Pokemon` con los atributos `name`, `type`, `hp` y `attack`.
# añade el método attack, quita hp al pokemon objetivo, en base a attack del pokemon atacante
# añade el método `faint`, que imprime un mensaje cuando el pokemon objetivo tiene 0 hp. (al finalizar el método attack llamaremos al target.faint())

#Extras al ejercicio

#Añade el atrivuto 'defense', que resta attack en base al attack del pokemon atacante
#Añade el atributo 'recover_health', que suma puntos de hp, en base al desempeño en ataques

class Pokemon:
    def __init__(self,name,type,hp,attack_power,defense_power):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack_power = attack_power
        self.defense_power = defense_power

    def attack(self,target):
        effective_damage = max(0,self.attack_power - target.defense_power)
        target.hp -= effective_damage

        if effective_damage <= 0:
            print(f'{target.name} recieved 0 damage points (blocked all)')
        else:
            print(f'{self.name} attacked {target.name} for {effective_damage} damage (blocked {target.defense_power} damage)')
    
        if target.hp <= 0:
            target.faint()
        else:
            print(f'{target.name} has {target.hp} health points left')

    def recover_health(self,amount):
        self.hp += amount
        print(f'{self.name} has recovered {amount} health points. Current HP {self.hp}')

    def faint(self):
        if self.hp <= 0:
            print(f'{self.name} has fainted!')    

venusaur = Pokemon('Venusaur','grass/poison',80,100,76)
charizard = Pokemon('Charizard','fire/flying',78,99,82)
blastoise = Pokemon('Blastoise','water',79,103,98)
golem = Pokemon('Golem','rock/electric',80,120,95)

venusaur.attack(golem)
venusaur.attack(charizard)


