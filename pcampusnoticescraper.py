import bs4 as bs
import wget
import os
import urllib.request

all_notice_links = []
all_notice_name= []
all_files_download_links = []
sauce = urllib.request.urlopen("https://www.pcampus.edu.np").read()
soup = bs.BeautifulSoup(sauce,'lxml')
for side_links in soup.find_all("aside"):
#notice links <aside> tag
    u  = side_links.find_all("ul")
    #ul inside aside tag
    for u_list in u:
        lin = u_list.find_all("li")
        #li in ul tag
        for link in lin:
             p = link.find_all("a")
             for links in p:
                     all_notice_links.append(links.get("href"))
                     all_notice_name.append(links.text)

for p in all_notice_links:                 
        notic = urllib.request.urlopen(p).read()
        sp1 = bs.BeautifulSoup(notic,"lxml")
        for file_or_link in sp1.find_all("div",class_="entry-content"):
                download = file_or_link.find_all("a")
                for notice_download in download:
                     all_files_download_links.append(notice_download.get("href"))

#dow = zip(all_notice_name,all_files_download_links)
try:
        os.mkdir("pythonScrapednotice")
except:
        pass

os.chdir("pythonScrapednotice")
for name,url in dow:
    print('Downloading %s' % name)
    filw = wget.download(url)
