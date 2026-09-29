from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return f"Hello fro Flask..."

@app.route('/about')
def about():
    return f"<h1>About Page</h1>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Welcome, {name}!</h1>" 

@app.route("/report/<int:report_id>")
def report(report_id):
    return f"<h1>Report #{report_id}</h1>"
    
if __name__=="__main__":
    app.run(debug=True)


