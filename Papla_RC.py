
# coding: utf-8

# In[ ]:


class Doctor():
    def __init__(self, name):
        self.name = name
        if name == "Papla":
            self.name = "#checkboxdropdownDoc > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(25) > input:nth-child(1)"
            self.spec = "ginekologia"
    def Check(self, user):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('/home/username/firefox/firefox')
        import time
        try:
            driver = webdriver.Chrome()
        except:
            driver = webdriver.Firefox()
        time.sleep(3)
        driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_name("Login")
        elem.clear()
        elem.send_keys(credentials(user)[0])
        elem = driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(credentials(user)[1])
        elem = driver.find_element_by_name("IsAcceptedRule").click()
        elem = driver.find_element_by_partial_link_text('Zalo').click()
        time.sleep(2)
        elem = driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_id("City")
        select = Select(driver.find_element_by_id("City"))
        select.select_by_visible_text("Warszawa")
        time.sleep(2)
        
        
        elem = driver.find_element_by_css_selector("#checkboxdropdown > button:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".validate > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(1) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(2) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(3) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(4) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(5) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(7) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(9) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#confirmDepartment").click()
        time.sleep(2)
                
        select = Select(driver.find_element_by_id("ListOfSpecialities"))
        select.select_by_visible_text(self.spec)
        time.sleep(1)
        
        
        
        elem = driver.find_element_by_id("checkboxdropdownDoc").click()
        elem = driver.find_element_by_css_selector("#checkboxdropdownDoc > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        #elem = driver.find_element_by_partial_link_text('Zazna').click()
        driver.find_element_by_css_selector(self.name).click()

        elem = driver.find_element_by_css_selector("input.form-control")
        elem.clear()
        elem.send_keys("2018-08-08 - 2018-10-22")

        elem = driver.find_element_by_id("sbtn").click()


# In[ ]:


class Generic():
    def __init__(self,spec):
        self.spec = spec
    def Check(self, user):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import Select
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('/home/username/firefox/firefox')
        import time
        try:
            driver = webdriver.Chrome()
        except:
            driver = webdriver.Firefox()
        time.sleep(3)
        driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_name("Login")
        elem.clear()
        elem.send_keys(credentials(user)[0])
        elem = driver.find_element_by_name("Password")
        elem.clear()
        elem.send_keys(credentials(user)[1])
        elem = driver.find_element_by_name("IsAcceptedRule").click()
        elem = driver.find_element_by_partial_link_text('Zalo').click()
        time.sleep(2)
        elem = driver.get("https://online.enel.pl/Visit/New")
        elem = driver.find_element_by_id("City")
        select = Select(driver.find_element_by_id("City"))
        select.select_by_visible_text("Warszawa")
        time.sleep(2)
        
        elem = driver.find_element_by_css_selector("#checkboxdropdown > button:nth-child(1)").click()
        elem = driver.find_element_by_css_selector(".validate > li:nth-child(1) > div:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(1) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(2) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(3) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(4) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(5) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(7) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#appendhere > label:nth-child(9) > input:nth-child(1)").click()
        elem = driver.find_element_by_css_selector("#confirmDepartment").click()
        time.sleep(2)
        
        select = Select(driver.find_element_by_id("ListOfSpecialities"))
        select.select_by_visible_text(self.spec)
        elem = driver.find_element_by_css_selector("input.form-control")
        elem.clear()
        elem.send_keys("2018-08-08 - 2018-10-22")
        try:
            elem = driver.find_element_by_css_selector("#AcptRul").click()
        except:
            pass
        time.sleep(1)

        elem = driver.find_element_by_id("sbtn").click()


# In[4]:


def credentials(user):
    f = open("C:\_Research\_Models\\"+user+".txt")
    lines = f.readlines()
    login = lines[0].split()[0]
    password = lines[1].split()[0]
    f.close()
    return login, password

def Pap():
    papla = Doctor("Papla")
    papla.Check(user)
    
def higiena():
    higienistka = Generic("higiena jamy ustnej")
    higienistka.Check(user)
    
def derma():
    derma = Generic("dermatologia i wenerologia")
    derma.Check(user)
    
def endo():
    endo = Generic("endokrynologia")
    endo.Check(user)
    
    
def close():
    root.destroy()
    
def ShowButtons():
    root.deiconify()
    root.title('Doctor Selector')
    frame = tk.Frame(root)
    frame.pack()
    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=close)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Papla",
                   command=Pap)
    slogan.pack(side=tk.LEFT)
    dental = tk.Button(frame,text = 'Higienistka', command=higiena)
    dental.pack(side = tk.BOTTOM)
    
    dermatolog = tk.Button(frame,text = 'Dermatolog', command=derma)
    dermatolog.pack(side = tk.BOTTOM)
    
    endok = tk.Button(frame,text = 'Endokrynolog', command=endo)
    endok.pack(side = tk.BOTTOM)
    
    def sel():
        global user
        user = str(var.get())

    var = StringVar(value="1")
    R1 = Radiobutton(root, text="Maciuch", variable=var, value="Maciek",
                      command=sel)
    R1.pack( anchor = W )

    R2 = Radiobutton(root, text="Donat", variable=var, value="Kasia",
                      command=sel)
    R2.pack( anchor = W )

    label = Label(root)
    label.pack()


# In[3]:


import tkinter as tk
import sys
from tkinter import messagebox
from tkinter import *
root = tk.Tk()
root.geometry("300x150")
#root.iconbitmap('favicon.ico')
root.withdraw()

if __name__ == "__main__":
    ShowButtons()


root.mainloop()


# In[ ]:


""
