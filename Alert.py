#Alert system

import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

def load_mobilenet_model():
    # Load MobileNetV2 model pre-trained on ImageNet dataset
    model = MobileNetV2(weights='imagenet')
    return model

def preprocess_image(img_path):
    # Load and preprocess the input image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def classify_human(img_path, model):
    # Preprocess the image
    img_array = preprocess_image(img_path)

    # Make predictions
    predictions = model.predict(img_array)

    # Decode and print the top-3 predicted classes
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    print("Predictions:")
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i + 1}: {label} ({score:.2f})")

if __name__ == "__main__":
    # Replace 'path/to/your/image.jpg' with the path to the image you want to classify
    img_path = 'Python/People image.jpg'

    # Load MobileNetV2 model
    mobilenet_model = load_mobilenet_model()

    # Classify the human in the image
    classify_human(img_path, mobilenet_model)

