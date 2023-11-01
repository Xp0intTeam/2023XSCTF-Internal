import requests, re, io, socket
from urllib.parse import urlparse, unquote_plus
import os
from modules.Gophers import GopherAdapter 
from modules.files import LocalFileAdapter 


def check(url):
    try:
        s = requests.Session()
        s.mount("xsctf://", GopherAdapter())
        s.mount('file://', LocalFileAdapter())
        resp = s.get(url)
        assert resp.status_code == 200
        return(resp.text)
    except:
        return "SOME ISSUE OCCURED"
    
