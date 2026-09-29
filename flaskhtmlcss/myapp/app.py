from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",titleHtml="Ethical Hacking Course")



@app.route("/user/<namePython>")
def user(namePython):
    return render_template("user.html",nameHtml=namePython)


@app.route("/user/<name>/<int:agePython>")
def greetings(name,agePython):
    return render_template("greetings.html",nameHtml=name,ageHtml=agePython)


"Let's create a function where i can loop through a list of names and display them on the web page. "
"i will pass the list to html file, then inside it i will use jinja"
@app.route("/list")
def list():
    names = ["John", "Jane", "Doe", "Alice"]
    ages = [15, 30,13, 40]
    people=zip(names,ages)
    return render_template("list.html",peopleHtml=people)



if __name__ == "__main__":
    app.run(debug=True)
