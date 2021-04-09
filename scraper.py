import requests
from json2html import *
from bs4 import BeautifulSoup
import csv

class ProxyScraper:
    results = []

    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):

        content = BeautifulSoup(html, 'lxml')
        table = content.find('table')
        rows = table.findAll('tr')
        headers = [header.text for header in rows[0]]
        results = [headers]

        for row in rows:
            if len(row.findAll('td')) and ([data.text for data in row.findAll('td')]) not in results :
                self.results.append([data.text for data in row.findAll('td')])
            else :
                None


    def to_csv(self):
        with open('proxies.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.results)


    def run(self):
        response = requests.get('https://iptrade.zendesk.com/api/v2/channels/voice/stats/agents_activity.json',headers={'Authorization': 'Basic bWVlbmFsLnNoYXJtYUBidC5jb206V29uZGVyd29tYW5AMjM='})
        #print(response.json())
        html_data = json2html.convert(json=response.json())
        self.results = []
        self.parse(html_data)

        response = requests.get('https://iptrade.zendesk.com/api/v2/channels/voice/stats/agents_activity.json?page=2&per_page=100', headers={'Authorization': 'Basic bWVlbmFsLnNoYXJtYUBidC5jb206V29uZGVyd29tYW5AMjM='})
        html_data = json2html.convert(json=response.json())
        self.parse(html_data)

        self.to_csv()
