from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from selenium.common.exceptions import TimeoutException, WebDriverException
from urllib3 import exceptions
import json

def login(username, password):
    usernameBar = driver.find_element(By.XPATH, '//*[@id="login"]')
    usernameBar.send_keys(username)

    passwordBar = driver.find_element(By.XPATH, '//*[@id="password"]')
    passwordBar.send_keys(password)

    driver.find_element(By.XPATH, '/html/body/div[1]/table[1]/tbody/tr[1]/td/div/form/div[3]/input').click()

def navigate(checkAll):
    trainButton = driver.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[1]/td[1]/div/a')
    trainButton.click()

    if checkAll:
        boxs = driver.find_elements(By.CLASS_NAME, 'ui-link')
        for i in boxs:
            if i.get_attribute("onclick") != None:
                #print(i.get_attribute('onclick'))
                if i.get_attribute("onclick").startswith("toutcocher"):
                    i.click()


    beginButton = driver.find_element(By.XPATH, '//*[@id="btn_QCM"]')
    beginButton.click()

    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        driver.quit()
        ended = True
        print("Pas de questions disponibles")
        quit()
    except WebDriverException:
        print("premiere question")
    except exceptions.MaxRetryError:
        quit()

def get_id():
    return driver.find_element(By.XPATH, '//*[@id="id_question"]').get_attribute("value")

def get_answers():
    answers=[]
    try :
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ui-checkbox"]/label')))
    except TimeoutException:
        4+4
        #print("Answers not found!")

    anyAnswers = driver.find_elements(by=By.XPATH, value='//div[@class="ui-checkbox"]/label')
    answers = []
    
    for i in range(len(anyAnswers)):
        try:
            anyAnswers[i].click()
            anyAnswers[i].click()
            answers.append(anyAnswers[i])
        except WebDriverException:
            1+1
    return answers

def check_db():
    with open("data.json", "r") as json_file:
        data = json.load(json_file)

    if get_id() in data :
        check_answers_from_data(data, get_id())
        print("ID FOUND!!")
    else:
        check_random_answers()

def check_answers_from_data(data, id):
    answers = get_answers()
    print(answers)
    print(data[id])
    for i in answers:
        for j in data[id]:
            if i.text==str(j):
                i.click()
                print(i.text)
                print(j)

def check_random_answers():
    """answers=[]
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/label')))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/label')))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/label')))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div/label')))
    answers.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/label'))
    if EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/label')):
        answers.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/label'))
    if EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div/label')):
        answers.append(driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/label'))
    if EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[5]/div/label')):
        answers.append(driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/label'))
    random = randint(0, len(answers) - 1)
    answers[random].click()"""
    try :
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ui-checkbox"]/label')))
    except TimeoutException:
        4+4
        #print("Answers not found!")

    anyAnswers = driver.find_elements(by=By.XPATH, value='//div[@class="ui-checkbox"]/label')
    answers = []
    
    for i in range(len(anyAnswers)):
        try:
            anyAnswers[i].click()
            anyAnswers[i].click()
            answers.append(anyAnswers[i])
        except WebDriverException:
            1+1
    random = randint(0, len(answers) - 1)
    answers[random].click()

def get_corrected_answers():
    corrected_answers_button = driver.find_element(By.XPATH, '//*[@id="btn_corriger"]')
    corrected_answers_button.click()
    answers=[]
    """WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/label')))
    answers.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/label').text)
    answers.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/label').text)
    answers.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/label').text)
    answers.append(driver.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/label').text)"""
    try :
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="ui-checkbox"]/label')))
    except TimeoutException:
        4+4
        #print("Answers not found!")

    anyAnswers = driver.find_elements(by=By.XPATH, value='//div[@class="ui-checkbox"]/label')
    answers = []
    
    for i in range(len(anyAnswers)):
        try:
            anyAnswers[i].click()
            anyAnswers[i].click()
            answers.append(anyAnswers[i].text)
        except WebDriverException:
            1+1
    print(answers)
    good_answers = []
    for answer in answers:
        if answer.startswith("Bonne réponse"):
            good_answers.append(answer[14:])
    print(good_answers)
    with open("data.json", "r") as jsonFile:
        data = json.load(jsonFile)
    try :
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/h4/font')))
    except TimeoutException:
        print("0")
    id = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/h4/font').text[3:]
    data[id] = good_answers

    with open("data.json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

    driver.find_element(By.XPATH, '//*[@id="btn_suivant"]').click()

    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        driver.quit()
        ended = True
    except:
        print("question suivante")


username="Pangauwin"
password="da7d5"

ended = False
driverService = Service("./drivers/geckodriver.exe")
driver = webdriver.Firefox(service=driverService, firefox_binary="C:\Program Files\Mozilla Firefox/firefox.exe")
driver.get("http://www.ulysqcm.fr/")
checkAll = True


login(username, password)
navigate(checkAll)

while not ended:
    check_db()
    get_corrected_answers()
