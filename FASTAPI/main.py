import time
from starlette.staticfiles import StaticFiles
from fastapi import Depends, FastAPI, HTTPException, Request, Response, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from api.api_v1 import email, main, items, OAuth2, base_auth
from core.config import settings
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url='/docs',
    # redoc_url=None,
    description="This is a very fancy project, with auto docs for the API and everything",
    version="6.6.6",
)

app.mount('/static', StaticFiles(directory='static'), name='static')
# html  目录名    内部使用
app.add_middleware(GZipMiddleware, minimum_size=1000)
# app.add_middleware(HTTPSRedirectMiddleware)   # https wss
app.add_middleware(TrustedHostMiddleware, allowed_hosts=['*'])
app.add_middleware(  # 添加中间件
    CORSMiddleware,  # CORS中间件类
    allow_origins=['*'],  # 允许起源所有
    allow_credentials=True,  # 允许凭据
    allow_methods=["*"],  # 允许方法
    allow_headers=["*"],  # 允许头部
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print(request.client.host)
    print(request.client.port)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


async def get_token_header(user_agent: str = Header(None)):
    # user_agent:str=Header(None) 匹配 User-Agent
    if not user_agent.startswith('Mozilla'):  # 假超密令牌
        raise HTTPException(status_code=400, detail="user_agent header invalid")  # X令牌头无效


app.include_router(main.router)
app.include_router(email.router)
app.include_router(base_auth.router)
app.include_router(OAuth2.router)
app.include_router(
    items.router,
    prefix=settings.API_V1_STR,
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': "Not found"}}
)


@app.on_event("startup")
async def startup_event():
    print('start')


@app.on_event("shutdown")
def shutdown_event():
    # 不能使用async
    print('shutdown')


if __name__ == '__main__':
    # for route in app.routes:
    #     print(route.path_regex.pattern)
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)
    # uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info', reload=True)
# uvicorn main:app --reload
