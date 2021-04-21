"""使用简单工厂方法， 实现timo 和 police 两个英雄
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力

每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

每个英雄都一个speak_lines方法
调用speak_lines方法，不同的角色会打印（讲出）不同的台词
timo : 提莫队长正在待命
police: 见识一下法律的子弹"""

class Hero:
    hp=0
    power=0
    name=""
    def __init__(self,hp,power):
        self.hp=hp    #血量
        self.power=power   #攻击力
    def fight(self,enemy):
        self.hp = self.hp - enemy.power
        enemy.hp = enemy.hp - self.power
        if self.hp>enemy.hp:
            print(f"{self.name}打赢了,{self.name}的血量还有{self.hp},敌人{enemy.name}的血量只有{enemy.hp}")
        elif enemy.hp>self.hp:
            print(f"{enemy.name}打赢了,{self.name}的血量只有{self.hp},敌人{enemy.name}的血量还有{enemy.hp}")
        else:
            print("打成了平局")
    def speal_lines(self):
        pass

class Timo(Hero):
    name = "Timo"
    def speal_lines(self):
        print("提莫队长正在待命")
class Police(Hero):
    name = "Police"
    def speal_lines(self):
        print("见识一下法律的子弹")
