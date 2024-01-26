from flask import Flask

app = Flask(__name__)

@app.route('/predict_weather', methods=['GET'])
def predict_weather():
  return Println('Hello  World')

if __name__ == '__main__':
    app.run(debug=True)
