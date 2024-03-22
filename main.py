import sys
import os
import os.path
sys.path.append('modules')
from html_parser import *
from ocr import *
from dotenv import load_dotenv 
import requests


try:
    load_dotenv()
    key   = os.environ.get('KEY1')
    endpoint = os.environ.get('ENDPOINT')
    url  = os.environ.get('URL')
    base_url = os.environ.get('BASE_URL')
    vendpoint = os.environ["VISION_ENDPOINT"]
    vkey = os.environ["VISION_KEY"]
except:
    print("Environment variables missing !")
    exit()




def analyse_file(file,vendpoint,vkey):
    txt_file=file[:-4]+".txt"
    if not os.path.isfile(txt_file):
        read=analyze_image_file(vendpoint,vkey,file)
        text="\n".join(["\n".join([f["text"] for f in e["lines"]]) for e in read["blocks"]])
        print(text)
        with open(txt_file, 'w') as handler:
            handler.write(text)

def main_fct():
    global vkey,vendpoint,url,base_url
    links=get_links(url,base_url)
    files=[]
    txt_files=[]

    for e in links:
        file=f'temp/{e.split("/")[-1]}.png'
        files.append(file)
        if not os.path.isfile(file):
            img_data = requests.get(e).content
            with open(file, 'wb') as handler:
                handler.write(img_data)

    for e in files:
        analyse_file(e,vendpoint,vkey)
        txt_files.append(e[:-4]+".txt")
    with open("index.txt", 'w') as handler:
        for i in range(len(files)):
            handler.write(files[i] + "\n")
            handler.write(txt_files[i] + "\n")

main_fct()