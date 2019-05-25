#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.display import clear_output
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[78]:


usr=input('Enter Email Id:')  
pwd=input('Enter Password:')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path = 'd:/chromedriver', options = chrome_options)
driver.get('https://www.facebook.com/') 
print ("Site Facebook aberto") 
time.sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email inserido") 
time.sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Senha inserida") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 


# In[88]:


com_texto = "troco"

val_minPrice = '1'
val_maxPrice = '1000'

val_latitude = '-19.899433'
val_longitude = '-43.957200'

val_radiusKM = '1000'

driver.get('https://www.facebook.com/marketplace/108069962559892/search/?query='+com_texto+'&minPrice='+val_minPrice+'&maxPrice='+val_maxPrice+'&latitude='+val_latitude+'&longitude='+val_longitude+'&categoryID=allelectronics&radiusKM='+val_radiusKM+'&vertical=C2C&sort=BEST_MATCH')


# In[89]:


# define parametros para o looping
continuar = True
ini = 0
fim = 100
height = 1000
last_height = 0

while continuar == True:
    
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, " + str(ini * height) + ");")
    
    clear_output()
    print(ini)
    
    if ini == fim:
        clear_output()
        print('O valor de fim definido como: ' + str(fim) + ' foi alcançado.')
        
        try:
            valor = int(input('Deseja definir um novo valor de fim: '))
        except:
            valor = 0
            
        if valor <= fim:
            continuar = False
            driver.execute_script("window.scrollTo(0, " + str(1 * height) + ");")
            print('Fim do deslocamento.')
        else:
            fim = valor
    
    ini += 1

a_childrens = driver.find_elements_by_tag_name('a')
for index in range(len(a_childrens)):
    #print(index)
    if a_childrens[index].get_attribute('href') != None:
        if a_childrens[index].get_attribute('href')[37:41] == "item":
            # Criando e escrevendo em arquivos de texto (modo 'w').
            arquivo = open('FB_Marketplace_Database.txt','a')
            arquivo.write(a_childrens[index].get_attribute('href') + "\t")
            try:
                arquivo.write(a_childrens[index].text.replace('\n','\t'))
            except:
                pass
            arquivo.write("\n")
            arquivo.close()

    clear_output()
print('Fim do carregamento.')


# In[90]:


driver.quit() 
print("Finalizado") 

