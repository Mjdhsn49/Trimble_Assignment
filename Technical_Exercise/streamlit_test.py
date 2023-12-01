import streamlit as st
import torch
from PIL import Image
from torchvision import transforms
from torchvision.models import vgg16
from transformers import AutoProcessor, CLIPModel
# Function to load and preprocess the image
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    return transform(image).unsqueeze(0)

# Function to perform inference with a custom model
def custom_inference(image):
    model = torch.load('Technical_Exercise/models/simple_model.pt',map_location=torch.device('cpu'))
    # Make the prediction
    with torch.no_grad():
            output = model(image)
            _, predicted_class = torch.max(output, 1)
    return predicted_class 

# Function to perform inference with VGG16
def vgg16_inference(image):
    model = torch.load('Technical_Exercise/models/vgg16_model.pt',map_location=torch.device('cpu'))
    with torch.no_grad():
        output = model(image)
        _, predicted_class = torch.max(output, 1)

    return predicted_class

# Function to perform inference with CLIP
def clip_inference(image, text=['fields', 'roads']):
    processor = AutoProcessor.from_pretrained("openai/clip-vit-base-patch32")
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
    inputs = processor(text, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    probs = outputs.logits_per_image.softmax(dim=1)
    pred = torch.max(probs, 1)
    # Extract values and indices
    values = [tensor.item() for tensor in pred]
    max_value = max(values)
    max_index = values.index(max_value)
    return max_index, max_value

# Streamlit app
def main():
    st.title("Field and Road Classification App")
    class_names = ['fields', 'roads']

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform inference with custom model
     #   custom_result = custom_inference(preprocess_image(image))
     #   st.subheader("Simple Custom Model Output")        
     #   st.text(f'Predicted Label by simple model: {class_names[custom_result.item()]}')

        # Perform inference with VGG16
        with st.spinner("Predicting with VGG16.model please wait...."):
            vgg16_result = vgg16_inference(preprocess_image(image))
        st.subheader("Fine-tuned VGG16 Model Output")
        st.text(f'Predicted Label by Vgg16: {class_names[vgg16_result.item()]}')

        # Perform inference with CLIP
        with st.spinner("Predicting with CLIP model please wait......"):
            max_index, max_value = clip_inference(image)
        st.subheader("CLIP Model Output")
        st.text(f'Predicted Label by CLIP model: {class_names[max_index]} with probability: {round(max_value * 100, 2)}')
if __name__ == "__main__":
    main()
