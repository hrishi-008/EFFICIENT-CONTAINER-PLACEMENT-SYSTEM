from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # input_data = request.json.get('data')
        return jsonify({
            'test': 'test',
            'message': 'Success'
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# make a post request to the server
@app.route('/predict', methods=['POST'])
def predict_post():
    try:
        input_data = request.json.get('data')
        print(input_data)
        return jsonify({
            'test': 'test',
            'message': 'Success',
            'data': input_data
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
