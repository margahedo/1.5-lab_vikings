
# Soldier

import random

class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
    
        self.strength = strength
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage
        

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        Soldier.__init__(self, health, strength)
        
        self.name = name
    
    def receiveDamage(self, damage):
            
        self.health -= damage
        
        if self.health > 0:
            
            return self.name + ' has received ' + str(damage) + ' points of damage'
        
        if self.health <= 0:
       
            return self.name + ' has died in act of combat'
    
    def battleCry(self):
        
        return 'Odin Owns You All'
        
# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        
        Soldier.__init__(health, strength)
        
    def attack(self):
    
        return self.strength
    
    def receiveDamage(self, damage):
    
         if self.health <= 0:
       
            return self.name + ' A Saxon has received ' + str(damage) + ' points of damage'
         
         if self.health <= 0:
        
            return self.name + ' A Saxon has died in combat '
        

# War


class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        
        self.saxonArmy = []
        
    def addViking(self, Viking):
        
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        
        viking = random.choice(self.vikingArmy)
        
        saxon = random.choice(self.saxonArmy)
        
        result = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:

            self.saxonArmy.remove(saxon)

        return result

    def saxonAttack(self):
        
        saxon = random.choice(self.saxonArmy)
        
        viking = random.choice(self.vikingArmy)

        result = viking.receiveDamage(saxon.strength)

        if viking.health <= 0:

            self.vikingArmy.remove(viking)

        return result
        
    def showStatus (self):

        if len(self.saxonArmy) == 0:
            
            return "Vikings have won the war of the century!"

        elif len(self.vikingArmy)==0:
            
            return "Saxons have fought for their lives and survive another day..."

        else:
            
            return "Vikings and Saxons are still in the thick of battle."
        
        
    
