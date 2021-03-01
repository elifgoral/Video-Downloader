import requests
from bs4 import BeautifulSoup

def get_video_links(archive_url):
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('meta')   
    for link in links:
        link_str = str(link['content'])
        if "mp4" in link_str:
            return link_str

def get_video_name(archive_url):
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    names = soup.findAll('h1')
    for name in names:
        name_str = str(name['title'])
        return name_str


def download_video_izlesene(archive_url, video_links):   
    r = requests.get(video_links, stream = True)
    str_name = get_video_name(archive_url) + ".mp4"
    with open(str_name,'wb') as f: 
        f.write(r.content) 
    return


if __name__ == "__main__":
    archive_url = "https://www.izlesene.com/video/ezgi-moladan-enis-arikana-dogum-gunu-surprizi/10557053"
    video_links = get_video_links(archive_url)
    download_video_izlesene(archive_url, video_links)