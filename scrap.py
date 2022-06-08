from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from codeforces import api
from api_info import key,secret

users = (api.call("user.friends", key=key, secret = secret))

# selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
data=[]
for i in range(len(users)):
    driver.get("https://codeforces.com/profile/"+users[i])
    try:
        content = driver.find_element(By.CSS_SELECTOR, 'div._UserActivityFrame_counterValue')
        dat = content.text
        l = len(dat)
        num = int(dat[0:(l-8)])
        data.append({'solved':num, 'profile':users[i]})
    except:
        print("[-] User "+users[i]+" caused error, skipping...\n")

driver.close()
# Sorting the users by number of questions solved
def sortFunc(e):
    return e['solved']


data.sort(reverse=True,key = sortFunc)

# Getting output
fs = open("output.txt", "w")
fs.write("Username sorted by number of questions solved\n")
fs.write("------------------------------\n")
for i in range(len(users)):
    fs.write(data[i]['profile']+"\t\t"+str(data[i]['solved'])+"\n")

fs.close()