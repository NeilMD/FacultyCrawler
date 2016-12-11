from bs4 import BeautifulSoup
import shutil
import requests
import os

def faculty_first(url):
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    for tag in soup.find_all('a',id='fac_name'):
        tag = tag['style']
        index2 = tag.find(',') + 1
        print(tag[index2:])

def faculty_last(url):
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    for tag in soup.find_all('a',id='fac_name'):
        tag = tag['style']
        index2 = (tag.find(',') - len(tag) )
        print(tag[6:index2])



def faculty_department(url):
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    for tag in soup.find_all('a',id='fac_name'):
        index = url.rfind('/') + 1
        new_url = url[:index] + tag['href']
        link1 = requests.get(new_url)
        source_code1 = link1.text
        soup1 = BeautifulSoup(source_code1,'html.parser')
        first_link = soup1.find(string='Department:')
        if first_link != 'None':
            print(first_link.find_next().find_next(string=True))
        else:
            print('No Record')




def faculty_rank(url):
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    for tag in soup.find_all('a',id='fac_name'):
        index = url.rfind('/') + 1
        new_url = url[:index] + tag['href']
        link1 = requests.get(new_url)
        source_code1 = link1.text
        soup1 = BeautifulSoup(source_code1,'html.parser')
        first_link = soup1.find(string='Rank:')

        if first_link != 'None':
            print(first_link.find_next().find_next(string=True))
        else:
            print('No Record')

def faculty_status(url):
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    for tag in soup.find_all('a',id='fac_name'):
        index = url.rfind('/') + 1
        new_url = url[:index] + tag['href']
        link1 = requests.get(new_url)
        source_code1 = link1.text
        soup1 = BeautifulSoup(source_code1,'html.parser')
        first_link = soup1.find(string='Status:')
        if first_link != 'None':
            print(first_link.find_next().find_next(string=True))
        else:
            print('No Record')

def faculty_college(url):
    link = requests.get(url)
    source_code = link.text
    soup = BeautifulSoup(source_code,'html.parser')
    for tag in soup.find_all('a',id='fac_name'):
        index = url.rfind('/') + 1
        new_url = url[:index] + tag['href']
        link1 = requests.get(new_url)
        source_code1 = link1.text
        soup1 = BeautifulSoup(source_code1,'html.parser')
        first_link = soup1.find(string='College:')
        if first_link != 'None':
            print(first_link.find_next().find_next(string=True))
        else:
            print('No Record')

faculty_department('http://www.dlsu.edu.ph/faculty/fis/alpha_list.asp?letter=B')
