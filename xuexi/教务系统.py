'''
教务管理系统 —— 题目要求
总要求： 用面向对象的思想完成开发；管理在校学生的成绩信息；通过控制台菜单与用户交互。

1. 添加学生成绩
根据输入的学生姓名、语文成绩、数学成绩、英语成绩，把成绩记录到系统中。

1.1 输入：学生姓名、语文成绩、数学成绩、英语成绩
1.2 检查学生姓名是否已存在：不存在才添加；已存在则不添加
1.3 验证成绩范围：0–100 分
1.4 创建学生对象，并添加到系统
2. 修改学生成绩
根据输入的学生姓名，修改对应学生的成绩。

2.1 输入要修改的学生姓名
2.2 根据姓名查找该学生，显示其当前成绩信息
2.3 输入新的语文、数学、英语成绩
2.4 更新学生成绩数据
3. 删除学生成绩
根据输入的学生姓名，删除对应学生的成绩。

4. 查询指定学生成绩
根据输入的学生姓名，查找并输出对应学生的成绩。

4.1 输出格式必须是：
姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263
'''




class ScoreError(Exception):
    """分数不在 0-100 之间"""


class StudentNotFoundError(Exception):
    """系统里没有这个学生"""


def safe_int(prompt):
    """读一个整数，输错就让用户重输，绝不抛给调用方"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  输入的格式不正确，请重新输入")


def read_score(subject,prompt=None):
    prompt = prompt or f"请输入{subject}成绩: "
    while True:
        score = safe_int(prompt)
        if 0 <= score <= 100:
            return score
        print(f"{subject}成绩必须在0-100之间，你输入的成绩为{score}.")



class Student:
    def __init__(self, name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分:{self.chinese + self.math + self.english}"

    def new_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class StuManagement:
    def __init__(self):
        self.Students = []

    #排查是否重名
    def find(self,name):
        """按姓名找学生，找不到就抛 StudentNotFoundError"""
        for s in self.Students:
            if s.name == name:
                return s
        raise StudentNotFoundError(f"学生「{name}」不存在")

    #添加学生
    def add_student(self):
        name = input("请输入学生姓名：")

        #判断学生是否存在于列表当中
        for s in self.Students:
            if s.name == name:
                print("该学生已存在！请重新添加！")
                return

        chinese = read_score("语文")
        math = read_score("数学")
        english = read_score("英语")


        stu = Student(name,chinese,math,english)
        self.Students.append(stu)
        print("学生信息添加成功！")



    #修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：").strip()
        stu = self.find(name)
        print(f"当前成绩为：{stu}")

        chinese = read_score("语文", "请输入修改后的语文成绩：")
        math = read_score("数学", "请输入修改后的数学成绩：")
        english = read_score("英语", "请输入修改后的英语成绩：")

        stu.new_score(chinese,math,english)

        print("学生信息修改成功！")
        print(f"修改后的成绩为:{stu}")

    #删除学生成绩
    def del_student(self):
        name = input("请输入你要删除的学生姓名：").strip()
        stu = self.find(name)
        self.Students.remove(stu)
        print("删除成功！")


    #查询指定学生成绩
    def search_student(self):
        name = input("请输入你要查询的学生姓名：")
        stu = self.find(name)
        print(f"学生信息为{stu}")

    #展示所有学生
    def show_student(self):
        for s in self.Students:
            print(s)

    #运行
    def run(self):
        print("欢迎使用教务系统~")
        print()
        while True:
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加学生 2.修改成绩 3.删除信息 4.查询指定学生 5.展示所有学生 6.退出 # ")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print()

            chiose = input("请选择操作（1-6）")
            try:
                match chiose:
                    case "1":#添加
                        self.add_student()
                    case "2":#修改
                        self.update_student()
                    case "3":#删除
                        self.del_student()
                    case "4":#查询指定
                        self.search_student()
                    case "5":#展示所有
                        self.show_student()
                    case "6":
                        break
                    case _:
                        print("操作输入错误请重新输入!")
            except ScoreError as e:
                print(f"操作失败：{e}")
            except StudentNotFoundError as e:
                print(f"操作失败：{e}")


if __name__ == "__main__":
    s = StuManagement()
    s.run()