import urllib.request
import re
import os

os.makedirs('images', exist_ok=True)

url = 'https://unsplash.com/s/photos/cleaning'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find image URLs matching rough unsplash photo format
    imgs = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9-]+[^"]*', html)
    # Filter for reasonable sizes and clean up duplicates
    valid_imgs = []
    for img in imgs:
        if 'w=' in img and 'h=' not in img and 'profile' not in img:
            base = img.split('?')[0]
            if base not in valid_imgs:
                valid_imgs.append(base)
    
    # Download 4 missing ones
    target_names = ['ai-scan.png', 'delivery.jpg', 'process.jpg', 'interior.jpg']
    for i, name in enumerate(target_names):
        if i < len(valid_imgs):
            img_url = valid_imgs[i] + "?w=800&q=80&fit=crop"
            print(f"Downloading {img_url} to images/{name}")
            urllib.request.urlretrieve(img_url, f"images/{name}")
except Exception as e:
    print("Error:", e)

