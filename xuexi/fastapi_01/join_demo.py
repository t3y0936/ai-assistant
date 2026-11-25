from sqlalchemy import func
from db import SessionLocal, Conversation, Message

db = SessionLocal()

rows = (
    db.query(
        Conversation.id,
        Conversation.title,
        func.count(Message.id).label("msg_count"),
    )
    .join(Message, Message.conversation_id == Conversation.id)
    .group_by(Conversation.id, Conversation.title)
    .order_by(func.count(Message.id).desc())
    .all()
)

for r in rows:
    print(r.id, r.title, r.msg_count)

db.close()