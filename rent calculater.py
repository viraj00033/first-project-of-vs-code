# Inputs needed from the user
import pymongo

# 1. MongoDB Connection Setup
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["my_flat_db"]
    collection = db["rent_records"]
    print("✅ MongoDB connected!")
except Exception as e:
    print("❌ Connection Error:", e)

# 2. User Inputs
rent = int(input("Enter hostel/flat rent = "))
food = int(input("Enter food amount = "))
electricity_spend = int(input("Enter electricity units = "))
charge_per_unit = int(input("Enter charge per unit = "))
persons = int(input("Enter number of persons = "))

# 3. Calculation
total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) / persons

print("Each person will pay =", output)

# 4. SAVE TO MONGO (Yeh part data MongoDB mein bhejta hai)
record = {
    "rent": rent,
    "food": food,
    "electricity_units": electricity_spend,
    "charge_per_unit": charge_per_unit,
    "total_persons": persons,
    "per_person_share": output
}

res = collection.insert_one(record)
print("🎉 Data MongoDB mein save ho gaya! ID:", res.inserted_id)