from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("form.html")
            
@app.route('/show_users')
def show_user_table():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/show_users')

if __name__ == "__main__":
    app.run(debug=True)