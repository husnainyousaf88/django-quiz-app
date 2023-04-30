import requests

url = "https://torcalnew.s3.eu-west-1.amazonaws.com/Etrasa/%7B13DB8CF9-9DEF-4BF9-A893-667E6DE099A1%7D.jpg"
filename = "image.jpg"

response = requests.get(url)
with open(filename, "wb") as f:
    f.write(response.content)
