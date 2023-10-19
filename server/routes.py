from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/register")
def register():
    response = jsonify(success=True)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
