# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas
from config import

def primary(sheet):
    #read and load csv into memory
    tempdf = pandas.read_csv(sheet)


    driver = webdriver.Chrome()
    driver.get("https://www.onlinecampaigntools.com/PDI")
    #loading and prep
    elem1 = driver.find_element(By.NAME, "UserName")
    elem2 = driver.find_element(By.NAME, "Password")
    elem1.send_keys("*")
    elem2.send_keys("*")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/div[4]/div/div[2]/fieldset/div[1]/div[3]/div/label/input").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/div[4]/div/div[2]/fieldset/div[1]/input[3]").click()
    WebDriverWait(driver, timeout=10)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/a/div/div/div[2]/p").click()
    WebDriverWait(driver, timeout=5)

    #loop
    #tempval is the PDI ID pulled from the list
    for row in tempdf.index:

    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[4]/div[3]/div[1]/input").send_keys(tempval)










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
