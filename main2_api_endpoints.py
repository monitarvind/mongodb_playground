from datetime import date, datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from bson import ObjectId
from main2_db_connect import user_list


app = FastAPI(title="Hello, my from FastAPI object")


class User(BaseModel):
    _id: str
    name: str
    email: EmailStr
    phone: int
    #dob: date

# @app.get("/")
# async def welcome():
#     return JSONResponse(status_code=200, content={"message": "Welcome"})

#To create a json user list
@app.post("/create_user")
async def create_user(user: User):
    result = user_list.insert_one(user.model_dump())
    return JSONResponse(status_code=200, content={"message": f"User added: {result.inserted_id}"})


#To get all the user data from MongoDB
@app.get("/")
async def userslist():
    users = []
    for user in user_list.find():
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        users.append(user)
    return JSONResponse(status_code=200, content={"users": users})

#Fetch any 1 user from DB
@app.get("/fetch_user/{user_id}")
async def fetchuser(user_id: str):
    user_data = user_list.find_one({"_id": ObjectId(user_id)})
    print(f"user_data: {user_data}")
    if user_data:
        user_data["_id"] = str(user_data["_id"])
        return JSONResponse(status_code=200, content={"message": "User found", "user": user_data})
    else:
        return JSONResponse(status_code=404, content={"message": "User NOT found"})
    


