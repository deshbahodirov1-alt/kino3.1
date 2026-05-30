import json


def load_movies():
    try:
        with open("movies.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

 
def save_movies(data):
    with open("movies.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# GROUPS LOAD
def load_groups():

    try:
        with open("groups.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except:
        return []


# GROUPS SAVE
def save_groups(data):

    with open("groups.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# USERS LOAD
def load_users():

    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except:
        return []


# USERS SAVE
def save_users(user_id, name):

    users = load_users()

    # USER BORLIGINI TEKSHIRISH
    for user in users:

        if user["id"] == user_id:
            return

    # YANGI USER QO'SHISH
    users.append({
        "id": user_id,
        "name": name
    })

    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)