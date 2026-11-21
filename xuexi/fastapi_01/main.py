from fastapi import FastAPI, Path,Query,Request,Depends,Header,HTTPException
import time
from pydantic import BaseModel,Field
from datetime import datetime
app = FastAPI(title="第一个 FastAPI 应用")


class ConversationCreate(BaseModel):
    title: str = Field(default="新对话", max_length=50, description="对话标题")
    persona: str = Field(default="", max_length=200, description="人设描述")

def get_current_user(x_token: str | None = Header(default=None)):
    if x_token != "secret-123":
        raise HTTPException(status_code=401, detail="未登录")
    return {"user_id": 1, "name": "t3y0936"}

conversations = {}      # 模块级

@app.post("/conversations")
def create_conversation(data: ConversationCreate):
    conv_id = datetime.now().strftime("%Y%m%d_%H%M%S%f")
    conversations[conv_id] = {
        "id": conv_id,
        "title": data.title,
        "persona": data.persona,
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    return conversations[conv_id]


@app.get("/conversations/{conv_id}")
def get_conversation(conv_id: str):
    if conv_id not in conversations:
        raise HTTPException(status_code=404, detail=f"对话 {conv_id} 不存在")
    return conversations[conv_id]

@app.get("/me")
def read_me(user: dict = Depends(get_current_user)):
    return user

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    cost = (time.perf_counter() - start) * 1000
    response.headers["X-Process-Time"] = f"{cost:.1f}ms"
    return response

@app.post("/conversations", summary="新建一个对话")
def create_conversation(data: ConversationCreate):
    return {
        "id": datetime.now().strftime("%Y%m%d_%H%M%S%f"),
        "title": data.title,
        "persona": data.persona,
        "messages": [],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
@app.get("/")
def read_root():
    return {"message": "hello"}


@app.get("/users/{user_id}")
def read_user(user_id: int, verbose: bool = False):
    return {
        "user_id": user_id,
        "verbose": verbose,
        "user_id 的类型": str(type(user_id)),
    }

@app.get("/user/hello")
def user_hello():
    return {"msg": "我正在学习 FastAPI ......"}

@app.get("/news/{news_id}")
async def get_news(news_id: int = Path(...,gt=0,le=100,description="新闻ID范围1~100")):
    return {"news_id": news_id, "title": f"新闻ID为{news_id}"}

@app.get("/news1/{news_name}")
async def get_item(news_name: str = Path(..., min_length=2, max_length=10, description="新闻名称范围2~10")):
    return {"news_name": f"新闻名称为{news_name}"}

@app.get("/book/query")
async def query_book(
    category: str = Query(
        default="Python开发",
        min_length=5,
        max_length=255,
        description="图书分类",
    ),
    price: float = Query(
        ...,
        ge=50,
        le=100,
        description="价格",
    ),
):
    return {"category": category, "price": price}

class Book(BaseModel):
    name:str = Field(min_length=2, max_length=20)
    author:str = Field(min_length=2, max_length=10)
    publisher:str = Field(default="咕咕嘎嘎出版社")
    price:float = Field(gt=0, description="价格")

@app.post("/book")
async def create_book(book: Book):
    return {"id": book.id,
            "author": book.author,
            "publisher": book.publisher,
            "price": book.price}

