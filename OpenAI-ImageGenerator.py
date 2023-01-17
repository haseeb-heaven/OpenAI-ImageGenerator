# This script uses the OpenAI API to generate images from a given prompt.
# The generated images will be saved in the current directory with the name "generated_image_i.jpg" where i is the index of the image.
# By default, the script generates 1 image, if no number of images is passed as argument.
# To use the script, you will need a valid OpenAI API key, Python 3.x, 'requests' library, 'PIL' library and 'argparse' library
# To run the script, provide the prompt and number of images as command line arguments using -p and -n flags respectively.
# Example : python openai_image_generation.py -p 'generate an image of sunset' -n 3

import argparse
import requests
import json
from PIL import Image
from io import BytesIO
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='This script generates images from a given prompt using the OpenAI API')
    parser.add_argument("-n", "--num_images", type=int, default=1, help="number of images to generate")
    parser.add_argument("-p", "--prompt", type=str, default='generate an image of a person holding an apple', help="prompt to generate image")
    parser.add_argument("-v", "--version", action="version", version='%(prog)s 1.0')
    parser.add_argument("-i", "--info", action="help", default=argparse.SUPPRESS, help="Show help and exit")

    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return args

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# The API endpoint to call
url = "https://api.openai.com/v1/images/generations"

# The headers to include with the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Get the command line arguments
args = parse_args()

# The data to include with the API request
data = """
{
    """
data += f'"model": "image-alpha-001",'
data += f'"prompt": "{args.prompt}",'
data += f'"num_images":{args.num_images},'
data += """
    "size":"256x256",
    "response_format":"url"
}
"""

# Send the request to the API
response = requests.post(url, headers=headers, data=data)

# Get the JSON response from the API
response_json = json.loads(response.text)

# Print the response
print(response_json)

# Get the URLs of the generated images from the response
image_urls = [image_data["url"] for image_data in response_json["data"]]

# Download and save the images from the URLs
for i, image_url in enumerate(image_urls):
    # Download the image from the URL
    response = requests.get(image_url)
    # Open the image using PIL
    image = Image.open(BytesIO(response.content))
    # Save the image to a file
    image.save(f"generated_image_{i}.jpg")
    print(f"Image {i} saved successfully!")
