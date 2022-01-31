from flask import Flask, jsonify, request

app = Flask(__name__)

buses = [
        {'number_plate': 'NAX 132',
        'manufacture': 'Toyota',
        'model': 'Hiace',
        'year': '2009',
        'capcity': 18},

        {'number_plate': 'JKX 531',
        'manufacture': 'Hyundai',
        'model': 'HR',
        'year': '2003',
        'capcity': 21},

        {'number_plate': 'HRT 352',
        'manufacture': 'Ford',
        'model': 'FordX',
        'year': '2016',
        'capcity': 20}
    ]


@app.route('/buses')
def get_buses():
    return jsonify(buses)

@app.route('/buses/<int:index>')
def get_bus(index):
    bus = buses[index]
    return jsonify(bus)


@app.route('/buses', methods=['POST'])
def add_bus():
    bus = request.get_json()
    buses.append(bus)
    return bus, 200

@app.route('/buses/<int:index>', methods=['PUT'])
def update_bus(index):
    bus_to_update = request.get_json()
    buses[index] = bus_to_update
    return jsonify(buses[index])

@app.route('/buses/<int:index>', methods=['DELETE'])
def delete_bus(index):
    deleted = buses.pop(index)
    return jsonify(deleted)



if __name__ == '__main__':
    app.run()





