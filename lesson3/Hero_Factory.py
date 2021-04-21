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
from lesson3.Hero import Police, Timo


class HeroFactory:
    def create_hero(self,hero):
        if hero=="timo":
            return Timo(1100,150)
        elif hero=="police":
            return Police(1200,120)
        else:
            raise Exception("此英雄不在工厂中")

#测试代码
if __name__== "__main__" :
    hero=HeroFactory()
    timo=hero.create_hero("timo")
    timo.speal_lines()
    police=hero.create_hero("police")
    police.speal_lines()
    timo.fight(police)
    timo.fight(police)
    timo.fight(police)
    timo.fight(police)
    police.fight(timo)

