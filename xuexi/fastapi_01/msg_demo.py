from db import SessionLocal, Message

db = SessionLocal()
rows = db.query(Message).filter(Message.conversation_id == 7).order_by(Message.id).all()
for m in rows:
    print(m.id, m.role, m.content[:20])
db.close()