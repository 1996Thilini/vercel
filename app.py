from flask import Flask, render_template, request, url_for, flash, redirect, session
import pyrebase

#initialize flask app
app = Flask(__name__)

#config in firebase
config = {
    "apiKey": "AIzaSyCkcghScc6rDrgb0x8b8bZ5gUt4s5tihtU",
    "authDomain": "fir-4-88c8d.firebaseapp.com",
    "projectId": "fir-4-88c8d",
    "storageBucket": "fir-4-88c8d.appspot.com",
    "messagingSenderId": "165675594303",
    "appId": "1:165675594303:web:27ec60d3d64209643ffe8a",
    "measurementId": "G-07ZGC1QLYM",
    "databaseURL":"https://fir-4-88c8d-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

#cookies session code
app.secret_key ="Thilini@16"

#create the login page..method is allow basically api to send a post request to it.. 
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('index2'))
            session['user'] =  email
        except:
            return 'Failed to login'
    return render_template('login.html')

@app.route('/register', methods=["POST","GET"])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
           user = auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('index'))
        except:
            return 'Failed to register' 
    return render_template('register.html')



db = firebase.database()
# data = {"nmmm":"Thilini Rashmika"}
# db.child("post").child("name").set(data)





@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        post = {
            "title":title,
            "content":content
        }
        try:
            db.child("Posts").push(post)
            return redirect(url_for('index2'))
        except:
            return render_template("create.html", message="Something wrong happened..!")

    return render_template("create.html")

@app.route('/home')
def index2():
    allposts = db.child("Posts").get()
    if allposts.val() == None:
        return render_template("home.html")
    else:
        return render_template("home.html", posts=allposts)


@app.route('/home/<id>')
def home(id):
    result = db.child("Posts").order_by_key().equal_to(id).limit_to_first(1).get()
    print(result)
    return render_template("post.html", data=result)



@app.route('/edit/<id>', methods=('GET', 'POST'))
def edit(id):
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        post = {
            "title":title,
            "content":content
        }
        db.child("Posts").child(id).update(post)
        return redirect("/home")

    result =  db.child("Posts").order_by_key().equal_to(id).limit_to_first(1).get()
    return render_template("edit.html", data=result)


@app.route('/delete/<id>', methods=["POST"])
def delete(id):
    db.child("Posts").child(id).remove()
    return redirect("/home")

if __name__ == '__main__':
    app.run(debug=True)
