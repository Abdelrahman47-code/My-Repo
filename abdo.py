from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://en.wikipedia.org/wiki/List_of_cuisines")
items = browser.find_elements(By.CLASS_NAME ,"div-col")

links = []
# print(len(items))

for item in items:
    keywords = [x.text.split("\n") for x in (item.find_elements(By.TAG_NAME, "ul"))]
#     print(len(keywords))
    for i in range(len(keywords)):
        for word in keywords[i]:
            word = word.replace(" ","_")
            link = f"https://en.wikipedia.org/wiki/{word}"
            links.append(link)
            
            
print(len(links))

f = open("links2.csv", 'w')
f.write("The Links\n")

for lk in links:
    f.write(lk+"\n")
    browser2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser2.get(lk)
    items2 = browser2.find_elements(By.TAG_NAME ,"ul")
    for item2 in items2:
        keywords2 = [x.text.split("\n") for x in (item2.find_elements(By.TAG_NAME, "li")) if len(x.text)>0]
        for i in range(len(keywords2)):
            for word2 in keywords2[i]:
#                 print(word2.split()[0])
                print(word2)
    browser2.quit()
    
f.close()
