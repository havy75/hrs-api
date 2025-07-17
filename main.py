from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from dotenv import load_dotenv  # ⬅️ Thêm dòng này để load .env

from routers import user_api  # ⬅️ Import router API

# Load biến môi trường từ file .env
load_dotenv()

app = FastAPI()

# Gắn router
app.include_router(user_api.router)

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
