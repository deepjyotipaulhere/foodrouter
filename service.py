from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import pymysql
import pymongo


app=Flask(__name__)
CORS(app)

def connectmysql():
    con=pymysql.connect(host='localhost', user='root', password='password123', db='food_hack',cursorclass=pymysql.cursors.DictCursor)
    return con

def connectMongo():
    con = pymongo.MongoClient('localhost', 27017)
    return con


@app.route("/")
def index():
    return "ok"

@app.route("/insertcustomer", methods=['POST'])
def insertcustomer():
    try:
        con=connectmysql()
        x=request.get_json()
        sql="INSERT INTO customer_details(Customer_Name, Contact_No, Creation_Date, Update_Date) VALUES('"+x['Customer_Name']+"',"+x['Contact_No']+",NOW(),NOW())"
        cur=con.cursor()
        cur.execute(sql)

        mongocon=connectMongo()
        coll=mongocon.user.login
        coll.insert_one({
            "username": x['username'],
            "password": x['password'],
            "userid": cur.lastrowid
        })
        con.commit()
        con.close()
        return "ok"
    except Exception as ex:
        return str(ex)
        return make_response(500, str(ex))


@app.route("/foodinspector", methods=['POST'])
def foodinspector():
    try:
        con=connectmysql()
        x=request.get_json()
        sql="INSERT INTO food_inspector( Company_Name, Hourly_charge, Zone,  Creation_Date, Update_Date) VALUES('"+x['Company_Name']+"',"+x['Hourly_charge']+",'"+x['Zone']+"',""NOW(),NOW())"
        print(sql)
        cur=con.cursor()
        cur.execute(sql)

        mongocon=connectMongo()
        coll=mongocon.user.login
        coll.insert_one({
            "username": x['username'],
            "password": x['password'],
            "userid": cur.lastrowid
        })
        con.commit()
        con.close()
        return "ok"
    except Exception as ex:
        return str(ex)
        return make_response(500, str(ex))

@app.route("/assignFoodInspector/<id>" , methods=['PUT'])
def assignFoodInspector(id):
    try:
        con = connectmysql()
        
        cur = con.cursor()
        # cur.execute ("Select emp_id from food_inspector where Zone_id in  (Select Zone_id from product_details product, location_details location where product.location_id = location.Location_id)")
        import random
        cur.execute("SELECT * FROM food_inspector")
        rv = cur.fetchall()
        sel=rv[random.randint(0,len(rv))]
        print(sel)
        sql="Update product_details set Assigned_food_inspector = "+str(sel['emp_id'])+" where product_id = " +str(id)
        print(sql)
        cur.execute(sql)
        p=cur.lastrowid
        con.commit()
        con.close()
        return jsonify(sel)
    except Exception as ex:
        print(str(ex))
        return str(ex)
        return make_response(500, str(ex))

@app.route("/insertproduct" , methods=['POST'])
def insertproduct():
    try:
        con=connectmysql()
        x=request.get_json()
        

        sql="INSERT INTO product_details(product_name, cooked, perishable, Creation_Date, Updation_Date , customer_id, location_id) VALUES('"+x['product_name']+"', '"+str(x['cooked'])+"',  '"+str(x['perishable'])+"', Now(), Now() , "+str(x['customer_id'])+","+str(x['selectedlocation'])+" )"
        print(sql)
        cur = con.cursor()
        cur.execute(sql)
        p=cur.lastrowid
        con.commit()
        con.close()
        return str(p)
    except Exception as ex:
        print(str(ex))
        return str(ex)
        return make_response(500, str(ex))



@app.route("/updateproduct/<id>" , methods=['PUT'])
def updateproduct(id):
    try:
        con=connectmysql()
        x=request.get_json()
        

        sql="Update product_details set Exipry_date = '"+x['exipry_date']+"', Verified = '"+x['Verified']+"' where product_id = " +str(id)
        print(sql)
        cur = con.cursor()
        cur.execute(sql)
        p=cur.lastrowid
        con.commit()
        con.close()
        return str(p)
    except Exception as ex:
        print(str(ex))
        return str(ex)
        return make_response(500, str(ex))


@app.route("/uploadimage/<id>", methods=['POST'])
def uploadimage(id):
    import os
    from werkzeug.utils import secure_filename
    try:
        import random
        x=request.files['test']
        xfilename=secure_filename(str(random.randint(1,1000))+str(hash(x.filename))+x.filename)
        x.save(os.path.join("C:\\Users\\Sudipta\\Desktop\\images",xfilename))

        con=connectmysql()
        cur=con.cursor()
        cur.execute("INSERT INTO image_store(Image_location, Product_id) VALUES('"+xfilename+"',"+str(id)+")")
        con.commit()
        con.close()
        return "http://10.1.3.206:8080/"+str(xfilename)
    except Exception as ex:
        return str(ex)


@app.route("/getProducts" , methods=['GET'])
def getProducts():
    try:
        con = connectmysql()
        cur = con.cursor()
        cur.execute("select * from (select CONCAT('http://10.1.3.206:8080/',image_location) as Image_Location,product_id from image_store group by product_id) img,product_details prd where img.product_id=prd.product_id and prd.Verified<>'-1' ")
        rv = cur.fetchall() 
        
        return jsonify(rv)
        
    except Exception as ex:
        return str(ex)

@app.route("/getProducts/<id>" , methods=['GET'])
def getProduct(id):
    try:
        product={}
        con = connectmysql()
        cur = con.cursor()
        cur.execute("SELECT * FROM Product_details prd,customer_details cust,location_details loc where Verified<>'-1' and prd.customer_id=cust.customer_id and prd.location_id=loc.location_id and product_id="+str(id))
        product=cur.fetchall()[0]
        cur.execute("SELECT CONCAT('http://10.1.3.206:8080/',image_location) as Image_Location from image_store where product_id = " +str(id))
        product['images']=cur.fetchall()
        # rv = cur.fetchall()
        
        return jsonify(product)
    except Exception as ex:
        return str(ex)

@app.route("/getorder/<id>")
def getorder(id):
    con=connectmysql()
    cur=con.cursor()
    cur.execute("SELECT * FROM order_header WHERE order_number="+id)
    order=cur.fetchall()[0]
    cur.execute("SELECT * FROM customer_details where customer_id="+str(order['sold_from_customer_id']))
    order['from']=cur.fetchall()[0]
    cur.execute("SELECT * FROM customer_details where customer_id="+str(order['Sold_to_customer_id']))
    order['to']=cur.fetchall()[0]
    cur.execute("SELECT * FROM location_details where Location_id="+str(order['Ship_to_location']))
    order['tolocation']=cur.fetchall()[0]
    cur.execute("SELECT * FROM location_details where Location_id="+str(order['Ship_from_location']))
    order['fromlocation']=cur.fetchall()[0]
    cur.execute("SELECT * FROM product_details where product_id="+str(order['Product_id']))
    order['product']=cur.fetchall()[0]
    cur.execute("SELECT CONCAT('http://10.1.3.206:8080/',image_location) as Image_Location from image_store where product_id = " +str(order['Product_id']))
    order['product']['image']=cur.fetchall()
    return jsonify(order)

@app.route("/orderverify/<id>/<val>")
def orderverify(id,val):
    con=connectmysql()
    cur=con.cursor()
    cur.execute("UPDATE product_details SET Verified='"+str(val)+"' WHERE product_id="+id)
    con.commit()
    con.close()
    return "ok"

@app.route("/login" , methods=['post'])
def getLogin():
    try:
        mongocon=connectMongo()
        coll=mongocon.user.login

        x = request.get_json()
        data = coll.find_one({'username':x['username'],'password':x['password']},{'_id':False})
        return jsonify(data)
    except Exception as ex:
        return str(ex)
        
@app.route("/getlocations")
def getlocations():
    con=connectmysql()
    cur=con.cursor()
    cur.execute("SELECT * FROM location_details")
    return jsonify(cur.fetchall())

@app.route("/price" , methods=['GET'])
def price():
    con = connectmysql()
    cur=con.cursor()
    cur.execute("SELECT * FROM pricing_table")
    return jsonify(cur.fetchall())



@app.route("/insertorder" , methods=['POST'])
def insertorder():
    try:
        con=connectmysql()
        x=request.get_json()
         
        data = con.cursor() 
        data.execute("Select pd.customer_id , pd.location_id from product_details pd, customer_details cd where pd.customer_id = cd.customer_id and product_id="+ x['productid'])

        rv = data.fetchall()[0]

        sql="INSERT INTO order_header(sold_from_customer_id, Sold_to_customer_id, Ship_to_location, Ship_from_location,Creation_Date, Update_Date,Product_id) VALUES('"+str(rv['customer_id'])+"', '"+x['to']+"',  '"+str(x['tolocation'])+"', '"+str(rv['location_id'])+"', Now(), Now(), '"+str(x['productid'])+"' )"
        # print(sql)
        cur = con.cursor()
        cur.execute(sql)
        p=cur.lastrowid
        con.commit()
        con.close()
        return str(p)
    except Exception as ex:
        print(str(ex))
        return str(ex)
        return make_response(500, str(ex))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    
