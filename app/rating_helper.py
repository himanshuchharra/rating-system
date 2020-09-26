from config import db


class Rating:
    def save_rating(self, collection_name, rating_to, rating_by, rating_value, ride_id):

        find_ride = db.db[collection_name].find_one({"ride_id": ride_id})
        if find_ride:
            return {'status': 'failed', 'code': 400, 'data': 'Rating already provided.'}
        else:
            db.db[collection_name].insert_one({"rating_to_id": rating_to, "rating_by_id": rating_by,
                                               "rating_value": rating_value, "ride_id": ride_id})
            return {'status': 'success', 'code': 200, 'data': "Thanks for rating."}

    def average_rating(self, collection_name, product_id):
        rating_sum = 0
        rating_avg = 0
        get_rating = db.db[collection_name].find({"rating_to_id": product_id}, {"rating_value": 1, "_id": 0})
        for value in get_rating:
            rating_sum += value['rating_value']
        if rating_sum:
            rating_avg = rating_sum/get_rating.count()
        return rating_avg


class User(Rating):
    col_name = 'user_rating'
    def provide_rating(self, rating_to, rating_by, rating_value, ride_id):
        response_rating = self.save_rating(self.col_name, rating_to, rating_by, rating_value, ride_id)
        return response_rating

    def get_average_rating(self, user_id):
        response_average = self.average_rating(self.col_name, user_id)
        return {'status': 'success', 'code': 200, 'data': {'average_rating': response_average}}


class Driver(Rating):
    col_name = 'driver_rating'
    def provide_rating(self, rating_to, rating_by, rating_value, ride_id):
        response_rating = self.save_rating(self.col_name, rating_to, rating_by, rating_value, ride_id)
        return response_rating

    def get_average_rating(self, driver_id):
        response_average = self.average_rating(self.col_name, driver_id)
        return {'status': 'success', 'code': 200, 'data': {'average_rating': response_average}}
