from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DB_NAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

students_collection = db["students"]
companies_collection = db["companies"]



companies_collection = db["companies"]
benchmarks_collection = db["benchmarks"]
training_collection = db["training_recommendations"]
