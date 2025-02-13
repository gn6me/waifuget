import requests
import json
from term_image.image import from_url

# Get JSON data
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return(text)

#print(response)
def imageLoad(tag,rating):
    url = f"https://danbooru.donmai.us/posts/random.json?tags={tag}+1girl+rating:{rating}"
    try: # make sure fetch works
        response = requests.get(url)
        jprint(response.json())
        imageData = json.loads(jprint(response.json()))
        imageURL = imageData['file_url']
        image = from_url(imageURL)
        return image
    except:
        return
