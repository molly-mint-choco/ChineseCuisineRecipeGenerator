from flask import Flask, request, jsonify
from photo_detect.photo_detect import detect_ingredients
from photo_detect.openai_photo_detect import ingredient_assistant
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

@app.route('/recipe', methods=['POST'])
def recipe_geneartor():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo uploaded'}), 400
    
    photo = request.files['photo']
    photo_path = os.path.join('/tmp', photo.filename)
    photo.save(photo_path)

    additional_instructions = request.form.get('additional_instructions', '')
    
    try:
        recipe_details = ingredient_assistant(photo_path, additional_instructions)
        return jsonify(recipe_details)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(photo_path)

if __name__ == '__main__':
    app.run(debug=True, port=7000)