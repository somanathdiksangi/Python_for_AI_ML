from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")  
def home_page():
    return "this is my home page"

@app.route("/somu", methods=["POST"])  # Ensure "POST" is in uppercase
def operation():
    if request.method == "POST":  
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        result = first_name + last_name
        return jsonify(result=result)  

if __name__ == "__main__":
    app.run(debug=True)
