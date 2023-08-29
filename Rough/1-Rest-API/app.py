from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [

]

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'prize': data['prize']}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

class ItemList(Resource):
    def get (self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')   # http://localhost:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(port=5000)