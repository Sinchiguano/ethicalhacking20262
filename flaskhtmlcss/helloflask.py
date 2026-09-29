from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def home():
    return"<h1>Hello Flask</h1>"



@app.route('/search')
def search():
    q = request.args.get('q','')
    return f"Searching for: {q}"


if __name__== "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
