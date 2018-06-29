import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import sys
import os
import json

args = sys.argv
print('subscription_key: ' + args[1])
print('file_directry: ' + args[2])

# Replace <Subscription Key> with your valid subscription key.
subscription_key = args[1]
assert subscription_key

file_directry=args[2]
files = os.listdir(file_directry)

for file in files:
  # You must use the same region in your REST call as you used to get your
  # subscription keys. For example, if you got your subscription keys from
  # westus, replace "westcentralus" in the URI below with "westus".
  #
  # Free trial subscription keys are generated in the westcentralus region.
  # If you use a free trial subscription key, you shouldn't need to change
  # this region.
  vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
  
  analyze_url = vision_base_url + "analyze"
  
  # Set image_path to the local path of an image that you want to analyze.
  image_path = file_directry + file
  print(image_path)
  
  # Read the image into a byte array
  image_resize_path = "/tmp/resize_"+file
  print(image_resize_path)
  Image.open(image_path).resize((3000,2000)).save(image_resize_path)
  image_data = open(image_resize_path, "rb").read()

  headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
                'Content-Type': 'application/octet-stream'}
  params     = {'visualFeatures': 'Categories,Description,Color'}
  response = requests.post(
      analyze_url, headers=headers, params=params, data=image_data)
  response.raise_for_status()

  
  # The 'analysis' object contains various fields that describe the image. The most
  # relevant caption for the image is obtained from the 'description' property.
  analysis = response.json()
  f = open(image_path +".txt", 'w')

  try:
    print(analysis)
    f.write(json.dumps(analysis, indent=4))
    f.write("\n")
  except Exception:
    pass

  try:
    image_caption = analysis["description"]["captions"][0]["text"]
    print(image_caption)
    f.write(json.dumps(image_caption, indent=4))
    f.write("\n")
  except Exception:
    pass

  try:
    tags_caption = analysis["description"]["tags"]
    print(tags_caption)
    f.write(json.dumps(tags_caption, indent=4))
    f.write("\n")
  except Exception:
    pass

  try:
    categories_caption = analysis["categories"][0]["name"]
    print(categories_caption)
    f.write(json.dumps(categories_caption, indent=4))
    f.write("\n")
  except Exception:
    pass

  f.flush()
  f.close()

  os.remove(image_resize_path)
#  # Display the image and overlay it with the caption.
#  image = Image.open(BytesIO(image_data))
#  plt.imshow(image)
#  plt.axis("off")
#  _ = plt.title(image_caption, size="x-large", y=-0.1)
