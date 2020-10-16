import requests
from bs4 import BeautifulSoup
import os


def main():
    project_list = []
    url = 'https://github.com/cuiyubao?tab=stars'
    file_name = 'README.md'
    while len(url) > 0:
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        find_all = soup.find_all("div", class_='col-12 d-block width-full py-4 border-bottom')
        for item in find_all:
            project_url = 'https://github.com' + item.find(class_='d-inline-block mb-1').find('a').get('href')
            project_name = ''
            try:
                project_name = item.find(class_='py-1').find('p').text.strip()
            except:
                project_name = project_url
            project = ' [' + project_name + '](' + project_url + ')'
            project_list.append(project)

        turn_page = soup.find(class_='paginate-container').find_all(class_='btn btn-outline BtnGroup-item')
        if turn_page[len(turn_page) - 1].name != 'button':
            url = turn_page[len(turn_page) - 1].get('href')
        else:
            url = ''
    print(project_list)
    os.remove(file_name)
    with open(file_name, 'a', encoding='utf-8') as md:
        index = 1
        for project in project_list:
            md.write(str(index)+'. ' + project + '\n\n')
            index = index + 1


if __name__ == '__main__':
    main()
