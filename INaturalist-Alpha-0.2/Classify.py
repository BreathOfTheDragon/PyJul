import torch
import torchvision.transforms as transforms
from PIL import Image
import json
import os
from torchvision import models

device = torch.device("mps")

model_ft = models.resnet18(pretrained=False)
num_ftrs = model_ft.fc.in_features
model_ft.fc = torch.nn.Linear(num_ftrs, 3)  # Change 3 to the number of classes you have

model_ft.load_state_dict(torch.load('pollinator_resnet18.pth', map_location=device))
model_ft = model_ft.to(device)
model_ft.eval()

with open('./pollinators.txt') as f:
    class_names = f.read().splitlines()


data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def classify_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = data_transforms(image).unsqueeze(0)  # Add batch dimension

    image = image.to(device)

    with torch.no_grad():
        outputs = model_ft(image)
        _, preds = torch.max(outputs, 1)

    predicted_class = class_names[preds.item()]
    return predicted_class


image_path = './test.jpg'  # Replace with your image path
predicted_class = classify_image(image_path)
print(f'The predicted class is: {predicted_class}')
