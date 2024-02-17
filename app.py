import sqlite3, os,Login,Clubs

from flask import Flask, redirect, url_for, render_template, request, session, flash, g

# importing real time to create permanent session for perios of time
from datetime import timedelta
app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
miniwebsite_dir = os.path.join(current_dir, '..')
database_path = os.path.join(miniwebsite_dir, 'MiniWebsite', 'MiniEpic.db')
app.config['DATABASE'] = database_path

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
@app.route("/home")
def home():
    roleCheck = session.get("roleCheck", 0)
    username = session.get("username", "base")
    return render_template("home.html", roleCheck=roleCheck, username=username)


@app.route("/login", methods=["POST", "GET"])
def login():
    error_message = None
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]
        password = request.form["password"]

        roleCheck = Login.login(username, password)
        if roleCheck is not None:
            session["username"] = username
            session["roleCheck"] = roleCheck
            return redirect(url_for("home"))
        else:
            error_message = "Invalid username or password. Please try again."
    return render_template("login.html", error_message=error_message)


@app.route("/register", methods=["POST", "GET"])
def register():
    error_message2 = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        phone = request.form["phone"]

        if Login.validate_reg(email):
            roleCheck = Login.create_account(username, password, name, surname, email, phone)
            session["username"] = username
            session["roleCheck"] = roleCheck
            return redirect(url_for("home"))
        else:
            error_message2 = "Email Taken"
    return render_template("register.html", error_message2=error_message2)




@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if request.method == 'POST':
        score = 0
        for i in range(1, 11):
            answer = request.form.get('question{}'.format(i))
            if answer == 'Paris':  # Assuming correct answer is Paris for all questions
                score += 1
        return render_template('quiz_result.html', score=score)
    else:
        return "Error: Invalid request method"
    




@app.route("/logout")
def logout():
    if "username" in session:
        user = session["username"]
        flash(f"You have been logged out, {user}", "info")
        session.pop("username", None)
        session.pop("roleCheck", None)
    return redirect(url_for("home"))


@app.route("/clubs")
def clubs():
    clubList = []
    for item in Clubs.user_view_clubs():
        clubList.append(item)
    roleCheck = session.get("roleCheck", 0)
    username = session.get("username", "base")
    return render_template("clubs.html", clubList=clubList, roleCheck=roleCheck, username=username)


@app.route("/events")
def events():
    roleCheck = session.get("roleCheck", 0)
    username = session.get("username", "base")
    return render_template("events.html", roleCheck=roleCheck, username=username)


@app.route("/memberships")
def memberships():
    roleCheck = session.get("roleCheck", 0)
    username = session.get("username", "base")
    return render_template("memberships.html", roleCheck=roleCheck, username=username)


@app.route("/Quiz")
def quiz():
    return render_template('quiz.html')


@app.route("/profile", methods=["POST", "GET"])
def profile():
    roleCheck = session.get("roleCheck", 0)
    username = session.get("username", "base")
    update_message = None
    update_message2 = None
    error_message = None

    if request.method == "POST":
        if "phone" in request.form:
            phone = request.form["phone"]
            user_id = Login.get_user_id(username)
            Login.update_number(user_id, phone)
            update_message = "Phone Number Updated"

        elif "old_password" in request.form and "new_password" in request.form:
            old_password = request.form["old_password"]
            new_password = request.form["new_password"]
            user_id = Login.get_user_id(username)
            result = Login.update_password(user_id, old_password, new_password)
            if result == "valid":
                update_message2 = "Password Updated"
            elif result == "invalid":
                error_message = "Invalid Password"

    return render_template("profile.html", roleCheck=roleCheck, username=username,update_message2=update_message2, update_message=update_message, error_message=error_message)

#allows me to go through clubList
@app.template_filter('enumerate')
def jinja2_enumerate(iterable):
    return enumerate(iterable)

if __name__ == "__main__":
    app.run(debug=True)
