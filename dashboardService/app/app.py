from fastapi import FastAPI
from dashboardService.routes import driftRouterHtml

routers = (driftRouterHtml,)

app = FastAPI()
for router in routers:
    app.include_router(router.router)


@app.get("/health")
async def health():
    return {"healthy": True}
