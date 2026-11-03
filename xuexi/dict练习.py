from nt import remove

student = []
menu = '''
1.添加学生信息
2.修改学生信息
3.删除学生信息
4.查询学生信息
5.列出学生信息
6.统计班级成绩
7.退出系统
'''
print("欢迎使用教务管理系统")
print(menu)
while True:
    choice = input("请输入操作（1-7）:")
    match choice:
        case "1":
            stu_name = input("请输入学生姓名:")
            if stu_name in student:
                print("已存在该学生！请重新输入！")
                continue
            else:
                chinese_sorce = input("请输入语文成绩：")
                math_sorce = input("请输入数学成绩：")
                english_sorce = input("请输入英语成绩：")
                if chinese_sorce.isdigit() and math_sorce.isdigit() and english_sorce.isdigit():
                    new_stu = {
                        "name": stu_name,
                        "chinese":float(chinese_sorce),
                        "math":float(math_sorce),
                        "english":float(english_sorce)
                    }
                    student.append(new_stu)
                    print("录入成功！")
                else:
                        print("必须输入纯数字！")
                        continue

        case "2":
            stu_name = input("请输入要修改的学生姓名:")

            for stu in student:
                if stu["name"] == stu_name:

                    new_chinese = input("请输入新的语文成绩:")
                    new_math = input("请输入新的数学成绩:")
                    new_english = input("请输入新的英语成绩:")

                    if new_chinese.isdigit() and new_math.isdigit() and new_english.isdigit():
                        stu["chinese"] = float(new_chinese)
                        stu["math"] = float(new_math)
                        stu["english"] = float(new_english)
                        print("修改成功！")
                    else:
                        print("错误！需要纯数字！")

                    break
            else:
                print("找不到该学生！")

        case "3":
            stu_name = input("请输入要删除数据的学生姓名：")
            for stu in student:
                if stu["name"] == stu_name:
                   student.remove(stu)
                   print("删除成功")
                   break
            else:
                print("找不到该学生！请重新输入！")

        case "4":
            stu_name = input("请输入要查寻的学生姓名：")
            for stu in student:
                if stu["name"] == stu_name:
                    print(f"姓名:{stu['name']},语文成绩:{stu['chinese']},数学成绩:{stu['math']},英语成绩:{stu['english']}")
                    break
                else:
                    print("找不到该学生！请重新输入！")

        case "5":
                if len(student) == 0:
                    print("当前系统里没用任何学生。")
                else:
                    print("---所有学生信息---")
                    for stu in student:
                        print(f"姓名:{stu['name']},语文成绩:{stu['chinese']},数学成绩:{stu['math']},英语成绩:{stu['english']}")

        case "6":
                if len(student) == 0:
                    print("当前系统里没用任何学生,无法统计！")
                    continue

                max_cn = student[0]["chinese"]
                min_cn = student[0]["chinese"]
                sum_cn = 0

                max_ma = student[0]["math"]
                min_ma = student[0]["math"]
                sum_ma = 0

                max_en = student[0]["english"]
                min_en = student[0]["english"]
                sum_en = 0

                max_chi_name = student[0]["name"]
                min_chi_name = student[0]["name"]
                max_math_name = student[0]["name"]
                min_math_name = student[0]["name"]
                max_eng_name = student[0]["name"]
                min_eng_name = student[0]["name"]

                for stu in student:
                    cn = stu["chinese"]
                    ma = stu["math"]
                    en = stu["english"]

                    sum_cn = sum_cn + cn
                    sum_ma = sum_ma + ma
                    sum_en = sum_en + en

                    if cn > max_cn:
                       max_cn = cn
                       max_chi_name = stu["name"]
                    if cn < min_cn:
                       min_cn = cn
                       min_chi_name = stu["name"]
                    if ma > max_ma:
                        max_ma = ma
                        max_eng_name = stu["name"]
                    if ma < min_ma:
                        min_ma = ma
                        min_eng_name = stu["name"]
                    if en > max_en:
                        max_en = en
                        max_eng_name = stu["name"]
                    if en < min_en:
                        min_en = en
                        min_eng_name = stu["name"]

                count = len(student)
                avg_cn = sum_cn / count
                avg_ma = sum_ma / count
                avg_en = sum_en / count

                print("---统计结果---")
                print(f"语文最高分为:{max_cn}({max_chi_name}),最低分为:{min_cn}({min_chi_name}),平均分为{avg_cn}")
                print(f"数学最高分为:{max_ma}({max_math_name}),最低分为:{min_ma}({min_math_name}),平均分为{avg_ma}")
                print(f"英语最高分为:{max_en}({max_eng_name}),最低分为:{min_en}({min_eng_name}),平均分为{avg_en}")

        case "7":
            print("再见，期待再次相遇~")
            break

