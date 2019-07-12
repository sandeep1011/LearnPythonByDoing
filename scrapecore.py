import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
# convert into text

soup = BeautifulSoup(source, "lxml")

csv_file = open('Scrapecore.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video_link'])

# print(soup.prettify())

# article = soup.find('article')

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    # .p for first paragraph
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']
    # print(vid_src)

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    # print(vid_id)

    yt_link = 'http://youtube.com/watch?v={}'.foramt(vid_id)
    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()




