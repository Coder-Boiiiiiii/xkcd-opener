#imports
import random
import webbrowser

#Code
comic_num = random.randint(1, 2462)
link = "https://xkcd.com/" + str(comic_num)

open = int(input("Open method (1 for link/ 2 to open in browser: "))
if open == 1:
    print("Link: " + link)

elif open == 2:
    webbrowser.open(link)
    print('link opened.')
