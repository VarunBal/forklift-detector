import flickrapi as flickr
import urllib
# import xml.etree.ElementTree as ET
# import cv2 as cv

key = '-API-KEY-'
secret = '-API-SECRET-'

flickr = flickr.FlickrAPI(api_key = key, secret = secret,)

def search(tags):
    pcount = 0
    ncount = 0
    
    photos =flickr.walk(tags = tags,tag_mode='all',per_page = 5000, extras='url_c')
    
    for idx,photo in enumerate(photos):
        try:
##                print('photo',photo.keys())
                pic_id=photo.get('id')
                
                owner_id=photo.get('owner')
                owner_info=flickr.people.getInfo(user_id=owner_id)[0]
##                ET.dump(owner_info)
                ispro=owner_info.get('ispro')
                
                sizes=flickr.photos.getSizes(photo_id=pic_id)[0]
##                    print(ET.dump(sizes))
                # size=sizes.find("./size[@label='Large Square']")
                size=sizes.find("./size[@label='Original']")
                url=size.get('source')
##                    print('small source:',url)

                urllib.request.urlretrieve(url, 'dataset\\flickr_img1\\flickr_'+str(pic_id)+".jpg")
                print(idx, 'pic saved')
        except Exception as e:
                print(e)
    print('pos:', pcount)
    print('neg:', ncount)
    print('total:', pcount+ncount)
    # cv.waitKey(0)

if __name__ == '__main__':
    urls = search('forklift')
