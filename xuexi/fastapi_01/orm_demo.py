from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3307/learn?charset=utf8mb4"

# echo=True：把生成的 SQL 打出来，这是你最快的学习方式
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, default="新对话")
    persona = Column(String(200), nullable=False, default="")
    created_at = Column(DateTime, default=datetime.now)


# 建表（已存在就跳过）
Base.metadata.create_all(engine)

db = SessionLocal()

# ---- 增 ----
c = Conversation(title="第一条记录", persona="温柔")
db.add(c)
db.commit()
print(">>> 新记录的 id =", c.id)      # 注意：commit 之后 id 才有值

# ---- 查 ----
rows = db.query(Conversation).all()
print(">>> 一共", len(rows), "条")
for r in rows:
    print(f">>> {r.id} | {r.title} | {r.persona} | {r.created_at}")

db.close()