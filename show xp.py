import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\HP\save file\sample\key.json") 
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user_xp(uid):
    user_ref = db.collection("users").document(uid)
    user = user_ref.get()

    if user.exists:
        data = user.to_dict()
        xp = data.get("xp", 0)
        coins = data.get("coins", 0)
        print(f"User {uid} → XP: {xp}, Coins: {coins}")
    else:
        print(f"No data found for UID: {uid}")

if __name__ == "__main__":
    uid = input("Enter User UID: ")
    get_user_xp(uid)
