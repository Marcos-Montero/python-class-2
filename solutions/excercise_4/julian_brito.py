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
            print(f'\n{target.name} loses, {self.name} wins\n')
        else:
            print(f'{target.name} has {target.hp} health points left')

    def recover_health(self,amount):
        self.hp += amount
        print(f'{self.name} has recovered {amount} health points. Current HP {self.hp}')

    def faint(self):
        if self.hp <= 0:
            print(f'\n{self.name} has fainted!\n')    

'Team Ash'
venusaur = Pokemon('Venusaur','grass/poison',190,110,76)
charizard = Pokemon('Charizard','fire/flying',190,99,82)

'Team Rocket'
blastoise = Pokemon('Blastoise','water',200,103,98)
golem = Pokemon('Golem','rock/electric',186,120,78)

print('''---First Combat Round---
        Ash: Golem I summon you!!
        Team Rocket: Venusaur to the game!!\n''')


venusaur.attack(golem)
golem.attack(venusaur)


print('''\n---Recovery Time---
        Team Rocket: Venusaur superglue health elixir
        Ash: Golem health meditating recovering tecnique
   \n''')


venusaur.recover_health(15)
golem.recover_health(15)


print('''\n---Second Combat Round---
        Ash: Here we go again!!
          Rocket Team: Bring it on!!\n''')


golem.attack(venusaur)
golem.attack(venusaur)



print('''\n---Rocket Team: They hit us twice, we need to attack!!!---\n''')


venusaur.attack(golem)
venusaur.attack(golem)
venusaur.attack(golem)



print('''\n---Announcer: Rocket Team has Ash team against the ropes---\n''')
print('''\n***Last Round---Fight till exhaustion---***\n''')


while golem.hp > 0 and venusaur.hp > 0:
    venusaur.attack(golem)
    if golem.hp <= 0:
        break
    golem.attack(venusaur)
    if venusaur.hp <=0:
        break
 









