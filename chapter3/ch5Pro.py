#!/usr/bin/env python3.5
# coding:utf-8
# 5.6.1
# 好玩游戏的物品清单
# 给定一个字典，包含物品名称和数量，并打印出数量对应的物品

dict_stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
print("5.6.1参考答案")
print('=' * 80)
print("给定字典：",dict_stuff)
print("运行结果：")
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + '\t' + k)
        item_total += v
    print("Total number of items:" + str(item_total))
displayInventory(dict_stuff)
print('=' * 80)
print()

# 5.6.2
# 将给定的列表添加到字典中去，并统计相同键对应的数量，最后统计总字典中值的总数
dragonLoot = ['gold coin','dagger','dagger','gold coin','gold coin','ruby','ruby']

print("5.6.2参考答案")
print('=' * 80)
inv = {'gold coin':42,'rope':1}
print("给定列表：",dragonLoot)
print("给定字典：",inv)
print("运行结果：")

# 按照SWI的思路,这里可以2种方法：
# 1是将列表转换成字典再操作
# 2是用setdefault方法将列表元素加到字典再进行元素个数的自增
# 在此感谢SWI的指点斧正。

def addToInventory(inventory,addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory
inv = addToInventory(inv,dragonLoot)
print(inv)
displayInventory(inv)
print('=' * 80)