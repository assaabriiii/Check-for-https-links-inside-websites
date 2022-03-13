import requests
from bs4 import BeautifulSoup
import os 
import easygui 


url = easygui.enterbox(msg="Enter website url : ")

entered_url = requests.get(url)


data = BeautifulSoup(entered_url.content , 'html.parser') 


data_b = data.find_all('a')

x = open('valids.txt' , 'w') 

for i in data_b :
    x.write(str(i.get('href'))+"\n") # it works for persian websites (Don't know why)
    
    
os.system(command="cat valids.txt | grep https > results.txt") # data that created as the main source 

with open('results.txt') as file :
    easygui.codebox(msg="All safe urls inside the website that clamied" , text=file.read())
    

