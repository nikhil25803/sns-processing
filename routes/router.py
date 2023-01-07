from fastapi import APIRouter, status, HTTPException, Request
from sqlalchemy.orm.session import Session
from fastapi import Depends
from db.database import get_db
from controllers import controller
import ast
import requests


router = APIRouter(tags=["notification"])


@router.post("/receive")
async def operation(request: Request, db: Session = Depends(get_db)):
    result = await request.json()
    if "SubscribeURL" in result.keys():
        URL = result["SubscribeURL"]
        requests.get(url=URL)
        print(result["SubscribeURL"])
    data = result["Message"]
    print(result)
    
    try:
        data = ast.literal_eval(data)
        data = ast.literal_eval(data["http"])
        car_number = data["car_number"]
        action = data["action"]
        if action == "INSERT":
            try:
                payload = controller.add_car(db=db, car_number=car_number)
                return {"Status": status.HTTP_201_CREATED, "Detail": payload}
            except:
                raise HTTPException(
                    status_code=status.HTTP_501_NOT_IMPLEMENTED,
                    detail="Unexpected Server Error",
                )
        if action == "REMOVE":
            try:
                payload = controller.delete_car(db=db, car_number=car_number)
                return {"Status": status.HTTP_202_ACCEPTED, "Detail": payload}
            except:
                raise HTTPException(
                    status_code=status.HTTP_501_NOT_IMPLEMENTED,
                    detail="Unexpected Server Error",
                )
        print("Hello")
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not authorised"
        )
