# importing google_images_download module 
from google_images_download import google_images_download 

# creating object 
rspns = google_images_download.googleimagesdownload() 

searchQuery = input("ENTER THE KEYWORD : ")
nm = input("ENTER NO. OF IMAGES YOU WANT TO DOWNLOAD : ")

def downloadImage(query):
    arg = {"keywords":query,"format": "jpg","limit":nm,"print_urls":False,"size": "medium","aspect_ratio": "panoramic"}
    #keyword is the search query
    #format is the image file format
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # size of images to download. ("tall, square, wide, panoramic") 
    try:
    #downloading images based on given arguments
        rspns.download(arg) 
	
    # Handling File NotFound Error	 
    except FileNotFoundError:
        arg = {"keywords":query,"format": "jpg","limit":nm,"print_urls":False,"size": "medium"}
					
    # Providing arguments for the searched query 
    try:
    #downloading images based on given arguments
            rspns.download(arguments) 
    except:
            pass

downloadImage(searchQuery)
