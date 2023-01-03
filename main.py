from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db import models
from routes import router
import uvicorn
from pyngrok import ngrok
import nest_asyncio

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():

    message = "Server running"
    return {
        "Status":status.HTTP_200_OK,
        "Message":message
    }


app.include_router(router.router)


models.Base.metadata.create_all(engine)

port = 8000
ngrok_tunnel = ngrok.connect(port)

print('Public URL:', ngrok_tunnel.public_url)

nest_asyncio.apply()

if __name__ == "__main__":
    uvicorn.run(app, port=8000)


