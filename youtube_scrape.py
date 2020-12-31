from selenium import webdriver 

url = "https://www.youtube.com/c/JakeBoly/training/videos
browser = webdriver.(Chrome) #browser = driver
browser.get(url) #tells browser to get sepecified url ^ 
browser.find_element_by_x_path('//*@id="thumbnail"]').click() #browser locates and clicks on video by (x_path)

