from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3307/learn?charset=utf8mb4"

engine = create_engine(DATABASE_URL, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, default="新对话")
    persona = Column(String(200), nullable=False, default="")
    created_at = Column(DateTime, default=datetime.now)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("建表完成")