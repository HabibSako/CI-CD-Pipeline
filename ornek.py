from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class PostalInfo(Resource):
    def get(self):
        return {
            'derslerim': [
                'Bulut Bilişim',
                'Oyun Geliştirme',
                'Açık Kaynak Yazılım Geliştirme',
                'Büyük Veri Teknolojileri'
            ]
        }

api.add_resource(PostalInfo, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
