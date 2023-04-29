
# 练习：往房子里面添加家具，并且实时计算剩余面积

class Furniture(object):
    '''家具类'''
    def __init__(self, name, area) -> None:
        self.name = name
        self.area = area
        print('')
        
class House(object):
    '''房子容器'''
    def __init__(self, house_type, total_area) -> None:
        self.house_type = house_type
        self.total_area = total_area
        self._free_area = total_area
        self._furniture_list = []
    
    def addFurniture(self, item: Furniture):
        if item.area > self._free_area:
            print('房间剩余空间不足，不能继续放置')
        else:
            print('空间够，继续放')
            self._free_area -= item.area
            self._furniture_list.append(item.name)
            
    def __str__(self) -> str:
        return ('房型:{},总面积:{},剩余面积:{},家具列表:{}'.format(self.house_type, self.total_area, self._free_area, self._furniture_list))



house1 = House('一室一厅', 50)

furn1 = Furniture('大床', 10)
furn2 = Furniture('书桌', 10)
furn3 = Furniture('化妆桌', 10)
furn4 = Furniture('衣柜', 20)
furn5 = Furniture('茶几', 10)
house1.addFurniture(furn1)  # 空间够，继续放
house1.addFurniture(furn2)  # 空间够，继续放
house1.addFurniture(furn3)  # 空间够，继续放
house1.addFurniture(furn4)  # 空间够，继续放
house1.addFurniture(furn5)  # 房间剩余空间不足，不能继续放置
print(house1)
# 房型:一室一厅,总面积:50,剩余面积:0,家具列表:['大床', '书桌', '化妆桌', '衣柜']



    
