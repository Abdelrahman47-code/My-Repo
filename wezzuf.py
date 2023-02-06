# https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=data%20analysis&start=0

# get the libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time


f = open('WebDevelopmentJobs.csv', 'w', encoding='utf-8')
header ='JobTitle, Company, Location, Time\n'
f.write(header)

def job_info(num, job):
    j_title = job.strip().replace(' ', '%20')

    for i in range(num):
        
        # set the url
        url = f'https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q={j_title}&start={i}'

        # set the page
        page = requests.get(url)

        # get the soup
        soup = BeautifulSoup(page.content, 'html.parser')


        # find the jobs
        jobs = soup.find_all('div', class_="css-1gatmva e1v1l3u10")

        for j in range(len(jobs)):
            # job information
            job_title = jobs[j].find('h2', class_="css-m604qf").text.strip().replace(', ', '-')
            company = jobs[j].find('a', class_="css-17s97q8").text.strip().split()[0]
            place  = jobs[j].find('span', class_="css-5wys0k").text.strip().replace(', ', '-')
            work = jobs[j].find('span', class_="css-1ve4b75 eoyjyou0").text.strip()

            f.write(job_title +','+ company +','+ place +','+ work +'\n')
    f.close()

job_info(30, 'digital marketing')
print('File Created')


# df = pd.read_csv('WebDevelopmentJobs.csv')
# print(df.head())