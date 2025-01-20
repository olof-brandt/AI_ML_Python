# prompt: use an appropriate pretrained neural network in pytorch to classify images of fruit. in the output, classify the object in the image with a text string using a good description. the image is a file in the directory

#funkade bra på
# 1. bananbild
# 2. katt
# 3. lokomotiv
# 4. grävling




#!pip install torch torchvision torchaudio

import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import requests
from io import BytesIO

# Load a pre-trained ResNet model
model = models.resnet18(pretrained=True)
model.eval()  # Set the model to evaluation mode

# Define image transformations (same as used during training)
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# ImageNet class labels
# You might need to download this file if you haven't already.
# The URL below points to a version of this file that is publicly accessible.
url = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
response = requests.get(url)
response.raise_for_status()  # Raise an exception for non-200 status codes

imagenet_labels = response.json()


def classify_image(image_path):
    try:
        img = Image.open(image_path)
        img_t = transform(img)
        batch_t = torch.unsqueeze(img_t, 0)

        # Make a prediction
        out = model(batch_t)

        # Get the predicted class index
        _, index = torch.max(out, 1)
        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

        # Get the class label
        class_index = index.item()
        predicted_class = imagenet_labels[class_index]
        confidence = percentage[class_index].item()

        # Return the result with a descriptive string
        return f"The image is classified as a {predicted_class} with {confidence:.2f}% confidence."
    except Exception as e:
        return f"Error classifying image: {e}"


# Example usage (replace with the actual path to your image file)
image_path = "../10.jpg"  #@param {type:"string"}
result = classify_image(image_path)
result