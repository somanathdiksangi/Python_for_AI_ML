from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")  
def home_page():
    return render_template('index.html')

@app.route("/somu", methods=["POST"])  # Ensure "POST" is in uppercase
def math_number():
    if request.method == "POST":  
        operation = request.form["operation"]
        first_num = float(request.form["first_num"])  # Convert string to float
        second_num = float(request.form["second_num"])  # Convert string to float
        
        # Perform operations
        if operation == "add":
            result = first_num + second_num
        elif operation == "sub":
            result = first_num - second_num
        elif operation == "mul":
            result = first_num * second_num
        elif operation == "div":
            if second_num != 0:  # Avoid division by zero
                result = first_num / second_num
            else:
                result = "Error: Division by zero"
        else:
            result = "Invalid operation"
    
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
