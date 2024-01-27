from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self, category_id=None):
        all_categories = {
            'Bulut Bilişim': ['Google Cloud', 'Docker', 'Jenkins', 'Snyk', 'DockerHub', 'ArgoCD'],
            'Oyun Geliştirme': ['Unity', 'C#', 'Hyper Casual Game'],
            'Açık Kaynak Yazılım Geliştirme': ['Git ve Github', 'NGINX', 'Flask', 'API'],
            'Büyük Veri Teknolojileri': ['Hadoop', 'Hive', 'HBASE', 'MONGODb']
        }

        if category_id is None:
            return all_categories
        elif category_id in all_categories:
            return {category_id: all_categories[category_id]}
        else:
            return {'error': 'Kategori bulunamadı.'}

api.add_resource(Product, '/', '/<string:category_id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)

