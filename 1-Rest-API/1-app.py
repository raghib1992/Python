from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


stores = [
    {
        'name': 'My Book Store',
        'items': [
            {
                'name': 'the secret',
                'prize': 379
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')
# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' :  request_data['name'],
        'items': 
            []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over stores
    # If stores matches return it
    # If stores not match, return error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({"Error": "Store not Found"})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {'name': , 'prize': }
@app.route('/store/<string:name>/items', methods=['POST'])
def create_store_in_items(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'prize': request_data['prize']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Error': 'No match found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({"Error": "Items not Found"})

app.run(port=3000)