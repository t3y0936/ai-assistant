# action = input("请输入动作")
# match action:
#     case "上"|"w"   |  "W":
#         print("角色向上移动")
#     case "下"|"s"   |  "S":
#         print("角色向下移动")
#     case "左" | "a" | "A":
#         print("角色向左移动")
#     case"右" | "d" | "D":
#         print("角色向右移动")
#     case "跳" | " " :
#         print("角色跳跃")
#     case "攻击" | "j" | "J":
#         print("角色发动攻击")
#     case "退出" | "esc" | "ESC":
#         print("角色退出")

# i = int(input("请输入等腰直角三角形的边长: "))
# for a in range(1,i+1):
#     for b in range(a):
#         print("*",end="  ")
#     print()
#
#


# i = int(input("请输入金字塔层数: "))
# for a in range(1,i+1):
#     for b in range(1,a+1):
#         print(b,end=" ")
#     print()


# n = 8
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i + j) % 2 == 0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()

# total = 0
# for i in range(1,1001):
#     if(i%5==0):
#         total += i
# print("所有的5的倍数累加等于：",total)




# text="akiwksjakdiklowiqaamnv bamvaxnsjdsjkaaxkjd"
#
# a=0;k=0
# for i in text:
#     if(i=="a"):
#         a=a+1
#     elif(i=="k"):
#         k=k+1
# print(f"字符串中有",{a},"个a")
# print(f"字符串中有",{k},"个k")

# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# new_list = list1 + list2 + list3
# print("合并后的列表的原始列表为：",new_list)
# new_list1=[]
# for i in new_list:
#     if i not in new_list1:
#         new_list1.append(i)
# new_list1.sort()
# print("去重合并之后的列表为：",new_list1)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# list2 = []
# list3 = []
#
# list2 = [i**2 for i in list1 if i%3==0 ]
# list3 = [i**2 for i in list1 if i%5==0 ]
#
# new_list = list2 + list3
# print("新列表为：",new_list)

# #-------------正确的且更加简便的写法------------------

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# # 只要能被3整除 或 能被5整除，就平方，一步到位
# new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
#
# print("新列表为：", new_list)

# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
#
# newList = [i for i in list1 if i > 0]
# newList.sort()
# print(newList)


# str1 = "黄山落叶松叶落山黄"
# str2 = "上海自来水来自海上"
# str3 = "上海自来水来自海"
#
#
# if str1 == str1[::-1]:
#     print("是回文")
# else:
#     print("不是回文")
# if str2 == str2[::-1]:
#     print("是回文")
# else:
#     print("不是回文")
# if str3 == str3[::-1]:
#     rint("是回文")
# else:
#     print("不是回文")


# result_list = []
# for i in range(10):
#     text = input("请输入第"+str(i+1)+"个字符串: ")
#     new_list = text[::-1].upper()
#     result_list.append(new_list)
# print("\n最终列表的内容是：")
# for item in result_list:
#     print(item)
