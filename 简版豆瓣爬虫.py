import requests
import json
def main():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1000"
    text = requests.get(url).text
    #print(text)
    path = r'D:\python\第7章 爬虫\第2节 scrapy框架\1.txt'
    python = json.loads(text)
    #print(python)
    for i in python:
        score = i.get('score')
        url = i.get('url')
        title = i.get('title')
        print(title,score,url)
        with open(path,'a') as f:
            f.write(title+'\t\t' + url +'\t'+score+'\n')

if __name__ == "__main__":
    main()