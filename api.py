import requests
import os
import dotenv
import json

dotenv.load_dotenv()

def check_license_plate(image:bytes) -> str:
    """ Takes image bytes, returns plate number  """
    URL = "https://api.platerecognizer.com/v1/plate-reader/" # API endpoint
    API_KEY = os.getenv("API_KEY") # Load API key env var

    # Make request
    response = requests.post(
        url = URL,
        data = dict ( regions = ["gb"] ),
        files = dict( upload = image),
        headers = {"Authorization": f"Token {API_KEY}"}
    )

    # Parse the plate number from the JSON response and return
    return json.loads(response.text)["results"][0]["plate"]

    
    
