shoppinglist = input("请扫描购买的物品： ")
goods = shoppinglist.split(",")
print("您购买的物品清单如下：")
for item in goods:
    item.strip()
    print(f"{item}")
