from flask import Flask, request, jsonify

app = Flask(__name__)

<<<<<<< HEAD
@app.route("/")  # Home route
=======
@app.route("/")  
>>>>>>> f413fe6a308b3bd4beca0e7843e42af477dcae14
def home_page():
    return "This is my home page."

@app.route("/somu", methods=["POST"])  # Ensure POST is specified correctly
def operation():
<<<<<<< HEAD
    if request.method == "POST":
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        result = first_name + last_name
        return jsonify(result=result)

@app.route("/math", methods=["POST"])  # Fixed the typo here
def add():
    if request.method == "POST":
        a = request.json["first_number"]  # Updated key for better clarity
        b = request.json["second_number"]  # Updated key for better clarity
        result = a + b
        return jsonify(result=result)
=======
    if request.method == "POST":  
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        result = first_name + last_name
        return jsonify(result=result)  
>>>>>>> f413fe6a308b3bd4beca0e7843e42af477dcae14

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for better error messages
