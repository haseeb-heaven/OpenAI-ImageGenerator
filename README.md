# OpenAI-ImageGenerator
OpenAI Image Generation is image generator using OpenAI to generate images from a given prompt.

## Prerequisites
- A valid OpenAI API key
- Python 3.x
- requests library
- PIL library
- argparse library

## Installation
Clone the repository
## Copy code
git clone `https://github.com/haseeb-heaven/OpenAI-ImageGenerator.git`</br>

## Install the required libraries
`pip install requests pillow`
Replace `YOUR_API_KEY` in the script with your actual API key

## Usage
To generate an image, run the script with the following command:

## Example
`python openai_image_generation.py -p 'generate an image of sunset' -n 3`</br>
The generated images will be saved in the current directory with the name generated_image_i.jpg where i is the index of the image.

By default, the script generates 1 image, if no number of images is passed as argument.

The script will also print the response of the API call.

## Note
The script generates images of size 256x256 pixels, if you want to change the size of the returned images you can change the "size" parameter in the data.

It's also worth noting that the OpenAI API has usage limits, check their pricing page for more information.

## Support
For any issues or queries, please open an issue on the GitHub repository

##  Contributions
All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

## Licensing
This project is licensed under the MIT License

Author
Haseeb Mir
