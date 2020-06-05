import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.amul.com/m/amul-hits?s=2020"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

images = soup.findAll('img')
for image in images:
    print(image['src'])
   
year = 2020
sub = "amul-hits"
ind = 1

while year>1980:
    for i in range(0,20):
        web = "https://www.amul.com/m/amul-hits?s="+str(year)+"&l="+str(i)
        response = requests.get(web)
        #response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.findAll('img')
        for image in images:
            #print image source
            if (image['src'].count(sub)>0):
                print(image['src'])
                #url = "https://www.amul.com/files/hits/amul-hits-2851.jpg"
                #response2 = requests.get(image['src'])
                #soup2 = BeautifulSoup(response2.text, "html.parser")
                #for image in soup.findAll("img"):
                    #print("Image: %(src)s" % image)
                #    image_url = urlparse.urljoin(url, image['src'])
                urllib.request.urlretrieve("https://www.amul.com/"+image['src'], r"C:\Users\admin\Desktop\projects\juggling\amul\\"+str(year)+'--'+str(ind)+".jpg")
                ind = ind + 1
        #print(web)
    year = year -1