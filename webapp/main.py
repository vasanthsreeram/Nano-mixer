from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def hello_world():
    if len(request.form) > 0:
        pass
    else:
        des_count=1
    return render_template("index.html",des_count=des_count,source_address="the nano address :3",source_amount=69,Destinations=[{"destination_address":"address 1","destination_amount":60},{"destination_address":"address 2","destination_amount":9}])

if __name__ == '__main__':
   app.run()