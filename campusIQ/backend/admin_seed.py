import asyncio
from app.database import students_collection
from app.utils.password_hash import hash_password

async def seed_admin():
    print("🌱 Seeding Admin User...")

    admin_email = "admin@campusiq.com"
    admin_password = "admin123"

    hashed = hash_password(admin_password)

    existing = await students_collection.find_one({"email": admin_email})

    if existing:
        await students_collection.update_one(
            {"email": admin_email},
            {
                "$set": {
                    "password": hashed,
                    "role": "admin"
                }
            }
        )
        print("✅ Admin updated in students collection")
        return

    admin_doc = {
        "name": "Admin User",
        "email": admin_email,
        "password": hashed,
        "role": "admin",
        "year": "N/A",
        "branch": "N/A",
        "cgpa": 0,
        "skills": [],
        "prs_score": 0
    }

    await students_collection.insert_one(admin_doc)
    print("✅ Admin created in students collection")

if __name__ == "__main__":
    asyncio.run(seed_admin())