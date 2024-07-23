from pymongo import MongoClient
from datetime import datetime

def insert_data():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local

    def find_books_by_genre(db, genre):
        books_collection = db.books
        query = {"genre": genre}
        projection = {"_id": 0, "title": 1, "author": 1}

        books = books_collection.find(query, projection)
        for book in books:
            print(book)

    def calculate_average_ratings(db):
        movies_collection = db.movies
        pipeline = [
            {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
            {"$sort": {"average_rating": -1}}
        ]

        results = movies_collection.aggregate(pipeline)
        for result in results:
            print(result)

    def user_actions_log(db, user_id, limit=5):
        user_actions_collection = db.user_actions
        query = {'user_id': user_id}
        sort_criteria = [("timestamp", -1)]

        actions = user_actions_collection.find(query).sort(sort_criteria).limit(limit)
        for action in actions:
            print(action)

    def books_count(db):
        books_collection = db.books
        pipeline = [
            {"$group": {"_id": "$year", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]

        results = books_collection.aggregate(pipeline)
        for result in results:
            print(result)

    def user_actions_change(db, user_id, date, old_action, new_action):
        user_actions_collection = db.user_actions
        query = {"user_id": user_id, "action": old_action, "timestamp": {"$lt": date}}
        update = {"$set": {"action": new_action}}

        result = user_actions_collection.update_many(query, update)
        print(f"업데이트 된 문서는 {result.modified_count} 개 입니다.")



    # find_books_by_genre(db, "fantasy")
    # calculate_average_ratings(db)
    # user_actions_log(db, 2)
    # books_count(db)
    user_actions_change(db, 1, datetime(2023, 4, 10), "view", "seen")

    client.close()

if __name__ == "__main__":
    insert_data()




