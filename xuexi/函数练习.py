# def socre(s):
#     if s>= 90:
#         print("A")
#     elif s>= 75:
#         print("B")
#     elif s>= 60:
#         print("C")
#     else:
#         print("D")
# socre(59)

# def word(w):
# #     if w == w[::-1]:
# #         return True
# #     else:
# #         return False
# #
# # word("lev")
# # print(word("lev"))

# def time_sec(s):
#     hours = s // 3600
#     minutes = (s % 3600) // 60
#     seconds = (s % 60)
#     return hours, minutes, seconds
# test_time = [60, 120, 180, 240, 300, 3661]
# for t in test_time:
#     hours, minutes, seconds = time_sec(t)
#     print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

def sjx(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a==b or a==c or b==c:
            return "等腰三角形"
        if a==b==c:
            return "等边三角形"
        else:
            return "普通三角形"
    else:
        return "无法构成三角形"

test_list= [(3,3,3),(4,5,2),(5,5,3),(2,1,1)]
for i in test_list:
    print(sjx(i[0],i[1],i[2]))



