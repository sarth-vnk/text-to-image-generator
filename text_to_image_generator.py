# Import necessary libraries
import requests
import base64

# Replace with your Hugging Face token
API_TOKEN = "YOUR_HUGGINGFACE_API_KEY"

# API endpoint
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# Headers
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Function to generate image from prompt
def generate_image(prompt):
    payload = {
        "inputs": prompt,
    }

    print("Generating image. Please wait...")

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        with open("generated_image.png", "wb") as f:
            f.write(response.content)
        print("✅ Image saved as 'generated_image.png'")
    else:
        print("❌ Failed to generate image.")
        print("Error:", response.json())

# Main code
if __name__ == "__main__":
    user_prompt = input("Enter a description for your image: ")
    generate_image(user_prompt)
