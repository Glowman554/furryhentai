import urllib.request
import re
import wget
from PIL import Image
import os

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')]

with opener.open(input("url >")) as response:
	ree = response.read()

search = re.findall(r"<p><img src=\".*\?", ree.decode())

files = []
for i in search:
	url = i.replace("<p><img src=\"", "").replace("?", "")
	files.append(wget.download(url))

images = []

for i in files:
	images.append(Image.open(i).convert("RGB"))

image0 = images[0]
images.remove(image0)

image0.save(input("output >"), save_all=True, append_images=images)

for i in files:
	os.remove(i)