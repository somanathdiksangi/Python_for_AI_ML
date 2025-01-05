from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")  
def home_page():
    return "this is my home page"

@app.route("/somu", methods=["POST"])  # Ensure "POST" is in uppercase
def math_number():
    if request.method == "POST":  
        operation = request.json["operation"]
        first_num = request.json["first_num"]
        second_num = request.json["second_num"]
        if operation=="add":
            result=first_num+second_num
        elif operation == "sub":
            result=first_num-second_num
        elif operation == "mul":
            result=first_num*second_num
        elif operation == "div":
              result=first_num/second_num
        else:
            print("give me correct option")
    return jsonify(result=result)  

if __name__ == "__main__":
    app.run(debug=True)