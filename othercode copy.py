import requests
from bs4 import BeautifulSoup
import webbrowser
import os

def get_page_content():
    urlinput = input("What URL do you want to pull from?")
    filename = input("What do you want this file to be called? (Please include file type)")
    page = requests.get(urlinput)
    soup = BeautifulSoup(page.content,'html.parser')
    newfile = open(filename, "w+")
    newfile.write(soup.prettify())
    def yesfunction():
        userinput = input("Do you want to open this file in your browser?")
        if userinput == "yes" or userinput == "Yes" or userinput == "y":
            webbrowser.open("file://" + os.path.realpath(filename))
            print("Your page has been downloaded successfully")
            return
        if userinput == "no" or userinput == "No" or userinput == "n":
            print("Your page has been downloaded successfully")
            return
        else:
            print("Please enter Yes or No")
            yesfunction()
    yesfunction()
    print("---Please note that if you would like to access a downloaded HTML file as HTML code, you must change "
          "your preferences in TextEdit under"
          "'Open' and then 'When Opening a File', and then open the file again in TextEdit---")

#http://kazuar.github.io/scraping-tutorial/
#use the above link to figure out how to add in login information

