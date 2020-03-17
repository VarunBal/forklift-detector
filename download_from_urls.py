import urllib.request
import os

save_dir = os.path.join('dataset', 'imagenet')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

with open('urls.txt') as f:
    for idx, url in enumerate(f, start=491):
        try:
            # urllib.request.urlretrieve(url,'dataset/'+str(idx+1)+'.jpg')
            req = urllib.request.Request(url)
            raw_img = urllib.request.urlopen(req).read()
            File = open(os.path.join(save_dir, str(idx+1) + ".jpg"), "wb")
            File.write(raw_img)
            File.close()
            print(idx+1,'image downloaded')
        except Exception as e:
            print(e)
        
input("Press Enter to exit...")
