from flask import Flask, request, jsonify
from config import db, rating_url_config
import rating_helper


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/RatingDatabase"
db.init_app(app)


@app.route('/rating/<product>', methods=["POST"])
def product_rating(product):
    try:
        error = validate_request_save_rating(product)
        if error:
            return jsonify(error)
        rating_to = request.form.get('rating_to_id')
        rating_by = request.form.get('rating_by_id')
        rating_value = int(request.form.get('rating_value'))
        ride_id = request.form.get('ride_id')
        run_class = getattr(rating_helper, str(product).title())
        response = run_class().provide_rating(rating_to, rating_by, rating_value, ride_id)
        return jsonify(response)
    except Exception as e:
        return {'status': 'failed', 'code': 500, 'data': 'Action failed'}


@app.route('/rating/<product>', methods=["GET"])
def rating_average(product):
    try:
        error = validate_request_get_rating(product)
        if error:
            return jsonify(error)
        product_id = request.args.get('product_id')
        run_class = getattr(rating_helper, str(product).title())
        response = run_class().get_average_rating(product_id)
        return jsonify(response)
    except Exception as e:
        return {'status': 'failed', 'code': 500, 'data': 'Action failed'}


def validate_request_save_rating(product):
    if product.lower() not in rating_url_config:
        return {'status': 'failed', 'code': 400, 'data': 'URL not supported.'}
    else:
        if not request.form.get('rating_to_id') or not request.form.get('rating_by_id') or not request.form.get(
                'rating_value') or not request.form.get('ride_id'):
            return {'status': 'failed', 'code': 400, 'data': {'error': 'field required', 'parameter': 'rating_to_id, '
                                                                                'rating_by_id, rating_value, ride_id'}}


def validate_request_get_rating(product):
    if product.lower() not in rating_url_config:
        return {'status': 'failed', 'code': 400, 'data': 'URL not supported.'}
    if not request.args.get('product_id'):
        return {'status': 'failed', 'code': 400, 'data': 'Provide product id.'}


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')
