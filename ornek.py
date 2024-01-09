from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kullanici.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

class Users(Resource):
    def get(self):
        users = User.query.all()
        data = [{'name': user.name, 'age': user.age, 'city': user.city, 'country': user.country, 'email': user.email} for user in users]
        return {'data': data}, 200

    def post(self):
        data = request.get_json()

        if not all(key in data for key in ['name', 'age', 'city', 'country', 'email']):
            return {'message': 'Eksik bilgi. Tüm alanları doldurun.'}, 400

        if not str(data['age']).isdigit():
            return {'message': 'Geçersiz yaş değeri.'}, 400

        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'Kayıt başarıyla eklendi.'}, 200

    def delete(self):
        data = request.get_json()

        if 'name' not in data:
            return {'message': 'Eksik bilgi. Name alanını doldurun.'}, 400

        user = User.query.filter_by(name=data['name']).first()

        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'Kayıt başarıyla silindi.'}, 200
        else:
            return {'message': 'Kayıt bulunamadı.'}, 404

class Cities(Resource):
    def get(self):
        cities = User.query.with_entities(User.city).distinct().all()
        data = [{'city': city[0]} for city in cities]
        return {'data': data}, 200

class Name(Resource):
    def get(self, name):
        user = User.query.filter_by(name=name).first()
        if user:
            data = {'name': user.name, 'age': user.age, 'city': user.city, 'country': user.country, 'email': user.email}
            return {'data': data}, 200
        else:
            return {'message': 'Bu isimle kayıt bulunamadı!'}, 404

class Email(Resource):
    def get(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            data = {'name': user.name, 'age': user.age, 'city': user.city, 'country': user.country, 'email': user.email}
            return {'data': data}, 200
        else:
            return {'message': 'Bu email ile kayıt bulunamadı!'}, 404

class Country(Resource):
    def get(self):
        countries = User.query.with_entities(User.country).distinct().all()
        data = [{'country': country[0]} for country in countries]
        return {'data': data}, 200

# Add URL endpoints
api.add_resource(Users, '/users')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/isim/<string:name>')
api.add_resource(Country, '/country')
api.add_resource(Email, '/email/<string:email>')

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=False)
