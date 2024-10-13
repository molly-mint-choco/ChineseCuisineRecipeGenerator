from google.cloud import vision
import os
from dotenv import load_dotenv
from google.oauth2 import service_account


def detect_ingredients(photo_path):
    load_dotenv()
    google_vision_api_key = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    credentials = service_account.Credentials.from_service_account_file(google_vision_api_key)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    with open(photo_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    objects = client.object_localization(image=image).localized_object_annotations
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return [label.description for label in labels],[object.name for object in objects]
