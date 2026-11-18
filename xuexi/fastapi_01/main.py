from fastapi import FastAPI, Path,Query

app = FastAPI(title="第一个 FastAPI 应用")


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

