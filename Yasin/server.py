from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_code', methods=['POST'])
def receive_code():
    data = request.get_json()
    code = data.get(code)

    # Call the function to stop the car when a color is detected
    if code == 1:
        stop_car()  # Replace this with the actual function to stop the car
    elif code == 2:
        # Add logic to handle green color
        print("Green color detected")
    elif code == 3:
        # Add logic to handle blue color
        print("Blue color detected")

    return f"Car control received for {code}"

def stop_car():
    # Add code here to stop the car (e.g., control GPIO pins)
    print("Car is stopping...")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

