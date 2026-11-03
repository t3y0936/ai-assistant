购物车管理系统开发
不一定！ 这完全取决于你当初选择用什么样的结构来存数据。

之前之所以一直让你用
for 循环，是因为你选择了“列表套字典”（students =[{"name": "张三"...}, {"name": "李四"...}]）。在列表里找东西，只能靠
for 循环一个个去翻。

但是，如果你觉得
for 循环太麻烦，你完全可以换一种更简单、更像“查字典”的方法！

还记得你最开始写购物车系统时，直接用的“纯字典”吗？
shopping_cart = {"苹果": {"price": 10}, "香蕉": {"price": 5}}
如果用字典来存学生，你就绝对不需要
for 循环了，一句 if 就能搞定！

给你对比一下两种方式：
方式一：你用列表套字典（必须用
for ）
python
students = [
    {"name": "张三", "chinese": 90},
    {"name": "李四", "chinese": 85}
]
# 想找张三，必须用 for 循环去挨个问：“你是张三吗？”
for stu in students:
    if stu["name"] == "张三":
        print("找到了")
方式二：你用纯大字典（不需要
for ）
python
students = {
    "张三": {"chinese": 90, "math": 95},
    "李四": {"chinese": 85, "math": 88}
}
# 想找张三，直接用他的名字当钥匙（键名）去开锁！
if "张三" in students:
    print("找到了！")
    print(students["张三"]["chinese"])  # 直接拿到90分
你看，如果用纯字典，根本不需要写那一长串的
for 循环，代码瞬间短了一大截！

如果你想改用“纯字典”写法，整个系统会变成这样：
如果你觉得纯字典好用，你要把最上面的
students = []
改成
students = {}。以后添加学生，直接用
students["张三"] = {成绩字典}。

下面是纯字典版本的核心逻辑，你可以看看有多清爽：

python
# 纯字典，键是名字，值是成绩字典
students = {}

# --- 添加 (不需要循环) ---
name = input("请输入姓名:")
if name in students:
    print("已存在该学生！")
else:
    chinese = input("请输入语文成绩:")
    # ...判断数字省略...
    students[name] = {"chinese": float(chinese)}  # 直接赋值添加
    print("添加成功")

# --- 修改 (不需要循环) ---
name = input("请输入要修改的姓名:")
if name in students:
    chinese = input("请输入新语文成绩:")
    students[name]["chinese"] = float(chinese)  # 直接修改
    print("修改成功")
else:
    print("没找到")

# --- 删除 (不需要循环) ---
name = input("请输入要删除的姓名:")
if name in students:
    del students[name]  # 直接删
    print("删除成功")
else:
    print("没找到")

# --- 查询 (不需要循环) ---
name = input("请输入要查询的姓名:")
if name in students:
    print(students[name])  # 直接查
else:
    print("没找到")
总结：到底选哪个？
列表套字典：每次找人、改人，都必须写一个
for 循环去遍历。代码长，但符合数据一行一行排列的真实情况。

纯字典：直接用名字当“身份证号”（键名），找、改、删、查全都是秒出结果，不用写任何
for 循环。

如果你实在讨厌写
for 循环，我强烈建议你把之前的列表[] 改成大字典 {}，整个系统的代码会简单得多！你想换吗？想换的话我直接给你写一份纯字典版本的完整代码。

本回答由
AI
生成，内容仅供参考，请仔细甄别
纯字典
太好了！选择纯字典是非常聪明的决定。用纯字典（把学生姓名当做键名），你就彻底告别了复杂的
for 循环遍历查找，代码会变得非常直观、简短。

下面这是完全基于你学过的知识（纯字典 + match...case + isdigit） 编写的完整代码。没有
for 循环，没有标记变量，你看一眼就能明白！

python
# 定义一个空的大字典，用来装所有学生
# 结构：{"张三": {"chinese": 90, "math": 95, "english": 88}, "李四": {...}}
students = {}


def show_menu():
    print("\n########## 教务管理系统 ##########")
    print("#         1. 添加学生信息         #")
    print("#         2. 修改学生信息         #")
    print("#         3. 删除学生信息         #")
    print("#         4. 查询学生信息         #")
    print("#         5. 列出所有学生         #")
    print("#         6. 统计班级成绩         #")
    print("#         7. 退出系统             #")
    print("##################################")


while True:
    show_menu()
    choice = input("请输入操作编号 (1-7)：")

    match choice:
        case "1":
            stu_name = input("请输入学生姓名：")

            # 判断名字在不在大字典的键里面
            if stu_name in students:
                print("已存在该学生！请重新输入！")
            else:
                chinese_str = input("请输入语文成绩：")
                math_str = input("请输入数学成绩：")
                english_str = input("请输入英语成绩：")

                if chinese_str.isdigit() and math_str.isdigit() and english_str.isdigit():
                    # 直接通过 名字 赋值，把成绩小字典存进去
                    students[stu_name] = {
                        "chinese": float(chinese_str),
                        "math": float(math_str),
                        "english": float(english_str)
                    }
                    print("录入成功！")
                else:
                    print("错误：成绩必须输入纯数字！")

        case "2":
            stu_name = input("请输入要修改的学生姓名：")

            if stu_name in students:
                chinese_str = input("请输入新语文成绩：")
                math_str = input("请输入新数学成绩：")
                english_str = input("请输入新英语成绩：")

                if chinese_str.isdigit() and math_str.isdigit() and english_str.isdigit():
                    # 直接通过 名字 找到里面的字典，然后修改
                    students[stu_name]["chinese"] = float(chinese_str)
                    students[stu_name]["math"] = float(math_str)
                    students[stu_name]["english"] = float(english_str)
                    print("修改成功！")
                else:
                    print("错误：成绩必须输入纯数字！")
            else:
                print("没找到这个学生，无法修改。")

        case "3":
            stu_name = input("请输入要删除的学生姓名：")

            if stu_name in students:
                del students[stu_name]  # 直接用 del 删掉这个名字及其对应的成绩
                print("删除成功！")
            else:
                print("没找到这个学生，无法删除。")

        case "4":
            stu_name = input("请输入要查询的学生姓名：")

            if stu_name in students:
                # 先取出这个人的成绩字典，方便后面打印
                stu_info = students[stu_name]
                print(f"姓名：{stu_name}，语文：{stu_info['chinese']}，数学：{stu_info['math']}，英语：{stu_info['english']}")
            else:
                print("没找到这个学生。")

        case "5":
            if len(students) == 0:
                print("当前系统里没有任何学生。")
            else:
                print("--- 所有学生信息 ---")
                # 这里必须用 for 循环，因为你得把所有学生打印出来（注意：这个 for 仅仅是用来打印的，不是用来查人的）
                for name in students:
                    info = students[name]
                    print(f"姓名：{name}，语文：{info['chinese']}，数学：{info['math']}，英语：{info['english']}")

        case "6":
            if len(students) == 0:
                print("没有学生数据，无法统计。")
                continue

            # 纯字典版本，在遍历时直接通过 items() 拿名字和字典
            max_chi = 0
            min_chi = 999
            sum_chi = 0

            max_math = 0
            min_math = 999
            sum_math = 0

            max_eng = 0
            min_eng = 999
            sum_eng = 0

            max_chi_name = ""
            min_chi_name = ""
            max_math_name = ""
            min_math_name = ""
            max_eng_name = ""
            min_eng_name = ""

            # 遍历纯字典，name 是键（名字），info 是值（成绩字典）
            for name, info in students.items():
                c = info["chinese"]
                m = info["math"]
                e = info["english"]

                sum_chi += c
                sum_math += m
                sum_eng += e

                if c > max_chi:
                    max_chi = c
                    max_chi_name = name
                if c < min_chi:
                    min_chi = c
                    min_chi_name = name

                if m > max_math:
                    max_math = m
                    max_math_name = name
                if m < min_math:
                    min_math = m
                    min_math_name = name

                if e > max_eng:
                    max_eng = e
                    max_eng_name = name
                if e < min_eng:
                    min_eng = e
                    min_eng_name = name

            count = len(students)
            avg_chi = sum_chi / count
            avg_math = sum_math / count
            avg_eng = sum_eng / count

            print("--- 统计结果 ---")
            print(f"语文最高分：{max_chi} ({max_chi_name})，最低分：{min_chi} ({min_chi_name})，平均分：{avg_chi}")
            print(f"数学最高分：{max_math} ({max_math_name})，最低分：{min_math} ({min_math_name})，平均分：{avg_math}")
            print(f"英语最高分：{max_eng} ({max_eng_name})，最低分：{min_eng} ({min_eng_name})，平均分：{avg_eng}")

        case "7":
            print("已退出系统，拜拜！")
            break

        case _:
            print("指令无效！请重新输入。")
纯字典版本爽在哪里？
查重 / 修改 / 删除 / 查询：完全不用写
for 循环！直接用 if stu_name in students: 就能判断有没有这个人。查找和修改直接
students[名字]，秒出结果。

只有“列出所有”和“统计” 这两个功能用到了
for 。为什么？因为你得把所有数据拿出来展示或计算，这就必须要把字典里的东西翻一遍。

students.items()
是个好东西：在
case
"6"
统计里，for name, info in students.items(): 这一句，可以同时把名字和成绩小字典拿出来，用起来非常顺手。

你可以把这段代码放到你的编辑器里跑一下，你会发现代码量比之前“列表套字典”少了很多，而且逻辑十分顺畅！


