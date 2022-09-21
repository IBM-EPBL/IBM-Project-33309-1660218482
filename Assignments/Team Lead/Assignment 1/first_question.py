
from flask import Flask, request, render_template
 
app = Flask(__name__)  
 
@app.route('/', methods =["GET", "POST"])
def get_info():
    if request.method == "POST":
       name = request.form.get("name")
       email = request.form.get("email")
       phone = request.form.get("ph_no")
       values = f"<h1>Name : {name}</h1><h1>Email : {email}</h1><h1>Phone Number : {phone}</h1>"
       return values
       
    return render_template("login.html")
 
if __name__=='__main__':
   app.run(debug=True)
