from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def hello_world():
    des_count = 1
    if request.form is not None:
        print(request.form)
        
    return render_template("index.html",des_count=des_count,source_address="the nano address",source_amount=69,Destinations=[{"destination_address":"address 1","destination_amount":60},{"destination_address":"address 2","destination_amount":9}])

if __name__ == '__main__':
   app.run(debug=True)