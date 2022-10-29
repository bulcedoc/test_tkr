from django.http import HttpResponse
from django.shortcuts import render
def home (request,key):
 roll = str(key).upper()
 from selenium import webdriver
 from selenium.webdriver.common.by import By
 from selenium.webdriver.chrome.options import Options
 options = Options()
 options.headless = True
 driver = webdriver.Chrome( options= options)
 driver.get("http://tkrec.in/")
 driver.find_element(By.XPATH,('//*[@id="login-username"]')).send_keys(roll)
 driver.find_element(By.XPATH,('//*[@id="login-password"]')).send_keys(roll)
 driver.find_element(By.XPATH,('//*[@id="loginform"]/div[3]/div/button')).click()
 driver.find_element(By.XPATH,('//*[@id="navbarNavDropdown"]/ul[1]/li[3]/a')).click()
 name = driver.find_element(By.XPATH,('/html/body/main/div[2]/div[1]/table/tbody/tr[3]/td[2]')).text
 per = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[1]'))
 classes = []
 for e in per[:-1]:
  classes.append(e.text)
 total_conducted = per[-1].text
 par = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[2]'))
 c_conducted = []
 for e1 in par[:-1]:
   c_conducted.append(e1.text)
 total_attended = par[-1].text
 pep = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[3]'))
 c_attended = []
 for e2 in pep[:-1] :
   c_attended.append(e2.text)
 total_per = pep[-1].text
 psp = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[4]'))
 c_per = []
 for e3 in psp:
   c_per.append(e3.text)
 driver.quit()
 dic = []
 i=0
 while i<len(classes):
    se={"subject":classes[i],
        "c_c" : c_conducted[i],
        "c_a" : c_attended[i],
        "c_p" : c_per[i]} 
    dic.append(se)
    i=i+1
 context = { 'name' : name,
             't_c': total_conducted,
             't_a': total_attended,
             't_p': total_per,
             'dic': dic
           }
 return render(request,'a_p.html',context)
def fun(request):
  return HttpResponse("Enter the rollnumber appending to the url")