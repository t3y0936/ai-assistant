from urllib.response import addbase


class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名:{self.name}，商品价格:{self.price}商品数量:{self.num}"


    def new_info(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

class ShoppingCart:
    def __init__(self):
        self.goods_list = []
    #添加商品
    def add_goods(self):
        name = input("请输入你要添加的商品名: ")
        #判断商品是否已存在
        for g in self.goods_list:
            if g.name == name:
                print("已经存在该商品，请重新添加！")
                return

        price = float(input("请输入商品价格: "))
        num = int(input("请输入商品数量: "))
        #验证价格和商品数量大于0
        if price >0 and num > 0:
            goods = Goods(name,price,num)
            self.goods_list.append(goods)
            print("商品添加成功！")
        else:
            print("商品添加失败，商品和价格必须要大于0，请重新添加！")

    #修改商品
    def update(self):
        name = input("请输入要修改的商品名:")
        for g in self.goods_list:
            if g.name == name:
                print(f"当前商品信息为{g}")

                price = float(input("请输入修改后的商品价格: "))
                num = int(input("请输入修改后的商品数量: "))

                # 验证价格和商品数量大于0
                if price > 0 and num > 0:
                    g.new_info(price,num)
                    print("商品修改成功！")
                    print(f"修改后的商品信息为：{g}")
                    return
                else:
                    print("商品修改失败，商品和价格必须要大于0，请重新修改！")
                    return
        print("未找到该商品！")

    #删除商品
    def del_goods(self):
        name = input("输入你想要删除的商品名： ")
        for g in self.goods_list:
            if g.name == name:
                self.goods_list.remove(g)
                print("删除成功！")
                return

        print("查无此商品，删除失败，请重新输入！")
    #查询商品
    def show(self):
        if len(self.goods_list) == 0:
            print("购物车为空！")
            return
        for g in self.goods_list:
            print(g)
    #运行
    def run(self):
        print("欢迎使用购物车系统~")
        print()
        while True:
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("#         1.添加商品 2.修改商品 3.删除商品 4.查询商品 5.退出         # ")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print()

            choice = input("请输入操作(1-5)")
            match choice:
                case "1":
                    self.add_goods()
                case "2":
                    self.update()
                case "3":
                    self.del_goods()
                case "4":
                    self.show()
                case "5":
                    break
                case _:
                    print("操作输入有误，请重新输入!")

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.run()

