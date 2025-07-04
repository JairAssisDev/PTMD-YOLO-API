from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from controller.controller_predict import router as routes_predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_predict)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)