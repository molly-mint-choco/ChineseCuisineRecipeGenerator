import requests

url = 'http://localhost:7000/detect'
file_path = 'image_samples/fruits/fruits1.jpg'

with open(file_path, 'rb') as photo:
    files = {'photo': photo}
    response = requests.post(url, files=files)

print(response.json())

# curl -X POST -F "photo=@fruits/fruits1.jpg" http://127.0.0.1:7000/detect

# curl -X POST -F "photo=@mix/mix1.png" -F "additional_instructions=Your instructions here" http://localhost:7000/recipe