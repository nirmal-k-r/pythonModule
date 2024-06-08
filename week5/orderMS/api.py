from flask import Flask #import library
from flask import jsonify
from flask import request

api = Flask(__name__) #create flask server

orders={
    '1': {
        'orderid': 1,
        'customer': 'John',
        'quantity': 100,
        'selling_price': 1000,
        'production_cost': 500,
        'num_defects': 10
    },
    '2':     {
        'orderid': 2,
        'customer': 'Jane',
        'quantity': 200,
        'selling_price': 2000,
        'production_cost': 1000,
        'num_defects': 20
    },
    '3':{
        'orderid': 3,
        'customer': 'Jack',
        'quantity': 300,
        'selling_price': 3000,
        'production_cost': 1500,
        'num_defects': 30
    },
    '4': {
        'orderid': 4,
        'customer': 'Jill',
        'quantity': 400,
        'selling_price': 4000,
        'production_cost': 2000,
        'num_defects': 40
    },
    '5': {
        'orderid': 5,
        'customer': 'Jim',
        'quantity': 500,
        'selling_price': 5000,
        'production_cost': 2500,
        'num_defects': 50
    }
}


#test route
@api.route('/', methods=['GET']) #define a route of type GET (url: http://localhost:3000/)
def test(): #define controller function
    return jsonify({'api': 'works'})


#retrieve all orders
@api.route('/orders',methods=['GET'])
def retrieve_orders():
    return jsonify(orders)

#retrieve one specific order
@api.route('/orders',methods=['POST'])
def retrieve_one_order():
    id=request.json['id']
    return jsonify(orders[id])


#add an order
@api.route('/orders/add',methods=['POST'])
def add():
    new_order=request.json['order']
    orderId=str(len(orders)+1)
    orders[orderId]=new_order
    return jsonify({'response': 'Successfully added'})

#delete an order
@api.route('/orders/delete',methods=['GET'])
def delete():
    id=request.args.get('id') 
    del orders[id]
    return jsonify({'response': 'Successfully deleted'})

#calculate average profit
@api.route('/orders/average_profit',methods=['GET'])
def average_profit():
    total=0
    for id,order in orders.items():
        total=total+(order['selling_price']-order['production_cost'])
    
    average_profit=total/len(orders)
    return jsonify({'average_profit': average_profit})



if __name__ == '__main__':
    api.run(port=3000) #run server on port 3000