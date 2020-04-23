import datetime
import pandas as pd
import requests
import argparse
from bs4 import BeautifulSoup
import os
import time

class CoronaDataScrap:

    def __init__(self):

    #    self.FORMAT = '[%(asctime)-15s] %(message)s'
     #   self.logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='bot.log', filemode='a')

        self.URL = 'https://www.mohfw.gov.in/'
        self.SHORT_HEADERS = ['Sno', 'Sno1', 'Name of State / UT',
                              'Total Confirmed cases (Including 77 foreign Nationals) ', 'Cured/Discharged/Migrated',
                              'Death']
        self.extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

        print("path :", os.getcwd())

    def scrap_data(self):


        parser = argparse.ArgumentParser()
        parser.add_argument('--states', default=',')
        args = parser.parse_args()

        response = requests.get(self.URL).content
        soup = BeautifulSoup(response, 'html.parser')
        header = self.extract_contents(soup.tr.find_all('th'))

        stats = []
        all_rows = soup.find_all('tr')
        for row in all_rows:
            stat = self.extract_contents(row.find_all('td'))
            if stat:
                if len(stat) == 5:
                    # last row
                    stat = ['', *stat]
                    stats.append(stat)
            #               elif any([s.lower() in stat[1].lower() for s in interested_states]):
            #                  stats.append(stat)

        corona_data = pd.DataFrame(data=stats, columns=self.SHORT_HEADERS)
        corona_data.drop(columns=['Sno', 'Sno1'], inplace=True)
        corona_data.to_csv('./DataScrap/corona_report.csv', index=False)
        time.sleep(2)

