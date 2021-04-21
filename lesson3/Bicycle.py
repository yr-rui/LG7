"""需求文档：
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入, 同时有两个方法：
1）fill_charge(vol) 用来充电, vol 为电量
2）run(km) 方法用于骑行,每骑行10km消耗电量1度,当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果"""

class Bicycle:
    def run(self,miles):
        print(f"人力骑行{miles}km")

class EBicycle(Bicycle):
    def __init__(self,cur_vol):
        self.cur_vol=cur_vol   #电动车当前电量
    def fill_charge(self,vol):
        """
        :param vol: 表示充电的电量
        :return:
        """
        # if isinstance(vol,int) or isinstance(vol,float):
        try:
            if vol >= 0:
                self.cur_vol = self.cur_vol + vol;
                if self.cur_vol > 100:  # 电量最多只能充满为100%
                    self.cur_vol = 100
                print(f"充电成功，充电后当前电量为{self.cur_vol}")
            else:
                # print("电量输入错误")
                raise Exception("充电电量输入不能为负数")
        except:
            print(f"充电失败，电量仍为{self.cur_vol}")

    def run(self,miles):
        """
        :param miles:需要骑行的公里数
        :return:
        """
        if miles>=self.cur_vol*10: #需要骑行的公里数大于电量可支撑的公里数，那么说明还需要人工骑行
            print(f"剩余电量不够骑行全程，电动骑行{self.cur_vol*10}km,",end="")
            super().run(miles-self.cur_vol*10)
            self.cur_vol=0
        else:
            self.cur_vol-=miles/10
            print(f"电动骑行{miles}km,骑行后电量还剩{self.cur_vol}%")

if __name__ == '__main__':

    bike=Bicycle()
    bike.run(3.3)
    ebike=EBicycle(50)
    ebike.run(1000)
    ebike.fill_charge(-30)
    ebike.fill_charge(0)
    ebike.fill_charge(14)
    ebike.fill_charge(99)
    ebike.run(900)
    ebike.run(200)