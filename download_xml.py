import requests
from bs4 import BeautifulSoup
import time


url = input("対象urlを入力してください")
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
elems = soup.find_all("div", class_='page_item')
base_url = "https://www.gpvweather.com/"
for elem in elems:
    time.sleep(1)
    target_url = elem.find(text="XML表示").previous_element.get("href")
    target_url = target_url.replace("./",base_url)
    response = requests.get(target_url)

    file_name = elem.text.split("気象庁")[0].replace("\xa0","").replace("/","").replace(" ","").replace(":","")
    print(file_name)
    file = open(f"{file_name}.xml","wb")

    #iter_content()メソッドでWebファイルのデータを渡す
    for chunk in response.iter_content(100000):
        #ファイル書込
        file.write(chunk)
        
    #ファイルを閉じる
    file.close()