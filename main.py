from pymongo import MongoClient

# Connect to DB Cluster (replace <db_password> with your actual password)
client = MongoClient("mongodb+srv://monitkk_db_user:3xZ4b73UrpLIMBzZ@mongodb.qxbrzx6.mongodb.net/")

db = client["dummy_db"]  # Select database (creates if doesn't exist)

emp_collection = db["emp_table"]  # Select collection (like a table)

# Insert a document (like a row)
#result = emp_collection.insert_one({"name": "Tanny Singh", "age": 29, })

#print(f"Inserted document ID: {result.inserted_id}")

# Insert many documents (like a row)
# result = emp_collection.insert_many([
#     {"name": "Tanny Singh", "age": 29},
#     {"name": "Manny Singh", "age": 28, "gender": "female"},
#     {"name": "Sanny Singh", "age": 27, "hobby": ["basket ball", "tennis"]},
#     {"name": "Aanny Singh", "age": 26, "job": "banking"}
# ])

# print(f"Inserted document IDs: {result.inserted_ids}")

# Insert json dict into DB
data2 = [
  {
    "_id": "004",
    "name": "J smith",
    "email": "js@gmail.com",
    "married": False,
    "weight": 81.0,
    "allergy": ["nuts"],
    "phone": "1234567890",
    "dob": "1992-12-21",
    "linkedin_url": "https://linkedin.com/js",
    "emergency_contact": 0,
    "calculated_age": 33
  },
  {
    "_id": "005",
    "name": "Marry john",
    "email": "marry@hdfc.com",
    "married": False,
    "weight": 69.0,
    "allergy": ["dogs", "stupid ppl"],
    "phone": "9876543210",
    "dob": "1992-12-21",
    "linkedin_url": "https://linkedin.com/marry_me",
    "emergency_contact": 911,
    "calculated_age": 33
  },
  {
    "_id": "006",
    "name": "Jackson",
    "email": "jack@gmail.com",
    "married": False,
    "weight": 96.0,
    "allergy": ["bee", "pollen"],
    "phone": "1298235700",
    "dob": "1990-12-21",
    "linkedin_url": "https://faceexample.com/jack",
    "emergency_contact": 700,
    "calculated_age": 35
  }
]

db2 = client["json_dict_db"]  # select or create db
data_collection = db2["user_details_coll2"] # creating a new collection

result = data_collection.insert_many(data2)

print(f"Your data has been inserted: {result.inserted_ids}")

