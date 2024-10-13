import requests

url = 'http://localhost:7000/detect'
file_path = 'image_samples/fruits/fruits1.jpg'

with open(file_path, 'rb') as photo:
    files = {'photo': photo}
    response = requests.post(url, files=files)

print(response.json())