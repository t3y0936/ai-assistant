# from secrets import choice
#
# shopping_cart = {}
#
# menu = (
#     '''
# ##########   购物车系统  ##########
# #          1. 添加购物车          #
# #          2. 修改购物车          #
# #          3. 删除购物车          #
# #          4. 查询购物车          #
# #          5. 退出购物车          #
# #################################
#     '''
# )
# print("欢迎使用购物车系统")
# while True:
#     print(menu)
#     choice = input("请输入操作（1-5）:")
#     match choice:
#         case "1":
#             item_name = input("请输入商品名:")
#             item_price = input("请输入商品价格:")
#             item_num = input("请输入商品数量:")
#             if item_name in shopping_cart:
#                 print("此商品已在购物车当中！")
#             else:
#                 shopping_cart[item_name] = {"price": item_price, "num": item_num}
#                 print("商品添加完毕！")
#
#         case "2":
#             item_name = input("请输入商品名:")
#
#             if item_name not in shopping_cart:
#                 print("此商品不在购物车当中！请重新输入！")
#                 continue
#
#             item_price = input("请输入商品价格:")
#             item_num = input("请输入商品数量:")
#             shopping_cart[item_name] = {"price": item_price, "num": item_num}
#             print("商品修改完毕！")
#
#         case "3":
#             item_name = input("请输入要删除的商品名:")
#             if item_name in shopping_cart:
#                 del shopping_cart[item_name]
#                 print("删除成功！")
#             else:
#                 print("查无此商品！无法删除,请重新输入！")
#                 continue
#         case "4":
#             item_name = input("请输入要查询的商品：")
#             for item in shopping_cart:
#                 print(f"商品名称:{[item_name]},商品价格:{[item_price]},商品数量:{[item_num]}")
#
#         case "5":
#             print("感谢使用，欢迎下次再见~")
#             break
#
#         case _:
#             print("指令无效！请重新输入。")
