# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# import speech_recognition as sr
# def open_google_and_search(text):
#     path = ChromeDriverManager().install()
#     search_for = text.split("kiếm", 1)[1]
#     speak('Okay!')
#     driver = webdriver.Chrome(path)
#     driver.get("http://www.google.com")
#     que = driver.find_element_by_xpath("//input[@name='q']")
#     que.send_keys(str(search_for))
#     que.send_keys(Keys.RETURN)
import webbrowser

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

query = input("Nhập từ khóa tìm kiếm trên Google: ")
search_google(query)