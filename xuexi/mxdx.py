class Student:
    def __init__(self,name,age,scores=None):
        self.name = name
        self.age = age
        self.scores = list(scores) if scores else []

    def say_hi(self):
        print(f"我是{self.name},今年{self.age}岁.")

    def avg_score(self):
        if len(self.scores) == 0:#if not self.scores:简洁版
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name}({self.avg_score()})"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age},{self.scores})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.avg_score() < other.avg_score()

s1 = Student("张三", 20, [80, 90])
s2 = Student("李四", 21, [70, 60])
assert s1.avg_score() == 85
assert str(s1) == "张三(85.0)"
assert s2 < s1
students = [s1, s2]
students.sort(reverse=True)
print([str(x) for x in students])   # ['张三(85.0)', '李四(65.0)']
