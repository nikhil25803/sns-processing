from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db import models
from routes import router
import uvicorn
import nest_asyncio
from pyngrok import ngrok
import boto3
from dotenv import load_dotenv
import os



load_dotenv('.env')
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
PUBLIC_URL = ngrok_tunnel.public_url
print('Public URL:', ngrok_tunnel.public_url)

nest_asyncio.apply()

sns = boto3.client("sns", 
                   region_name="ap-south-1", 
                   aws_access_key_id="",
                   aws_secret_access_key=""
)
# Access Key Whatsapp se dekh le

response = sns.subscribe(TopicArn="arn:aws:sns:ap-south-1:814090889453:naka-local-car-data", Protocol="HTTP", Endpoint=PUBLIC_URL+"/receive")
subscription_arn = response["SubscriptionArn"]
print(response)

# data = requests.get(response)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)


