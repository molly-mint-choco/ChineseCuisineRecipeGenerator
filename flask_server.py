from flask import Flask, request, jsonify
from photo_detect.photo_detect import detect_ingredients
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo uploaded'}), 400
    
    photo = request.files['photo']
    photo_path = os.path.join('/tmp', photo.filename)
    photo.save(photo_path)
    
    try:
        ingredients = detect_ingredients(photo_path)
        return jsonify({'ingredients': ingredients})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(photo_path)

if __name__ == '__main__':
    app.run(debug=True, port=7000)