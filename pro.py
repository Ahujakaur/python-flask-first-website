from flask import Flask, request, jsonify
import pymongo


from bson import json_util

app=Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#mydb=MongoConnect()
mydb = myclient["mydata"]

#route for post product
@app.route('/product',methods=['POST'])
def data():
    mycol=mydb["product"]
    n=request.json["proname"]
    t=request.json["protype"]
    w=request.json["proweight"]
    data={
        "proname": n,
        "protype": t,
        "proweight":w
    }
    x=mycol.insert_one(data)
    print(x)
    response={
        "id":str(x.inserted_id),
        "proname":n,
        'protype': t,
        'proweight':w
    }
    return response
#route for get product's database
@app.route('/product',methods=['GET'])
def all_products():
    mycol=mydb["product"]
    all_products=mycol.find()
    response=json_util.dumps(all_products)
    return response

#route for find any specific data
@app.route('/product/<name>',methods=['GET'])
def single_product(name):
    mycol=mydb["product"]
    all_products=mycol.find_one({
        "proname": name
    })
    response=json_util.dumps(all_products)
    return response
#route for delete any data
@app.route('/product/<name>',methods=['DELETE'])
def delete_product(name):
    mycol=mydb["product"]
    all_products=mycol.delete_one({
    "proname": name
    })
    return jsonify({"Message" :name+" is Deleted"})

#route for change in database
@app.route('/user/<name>',methods=['PUT'])
def update_product(name):
    mycol=mydb["product"]
    proname=request.json["proname"]
    protype=request.json["protype"]
    q=request.json["proweight"]

    data={
        "proname":n,
        'protype':t,
        'proweight':w
    }
    mycol.update_one({"proname":name},{"$set":data})
    return jsonify({"Message" :name+" is Updated"})


if __name__=='__main__':
    app.run(debug=True)
