import urllib.parse, urllib.request
import requests
import json

from requests_toolbelt.multipart.encoder import MultipartEncoder
import base64

import pycurl
import io
import os

def face_verify(photo1, photo2):
    
    url = 'https://api.findface.pro/v0/verify'

    c = pycurl.Curl()
    c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.URL, url)
    fout = io.BytesIO()
    c.setopt(pycurl.WRITEFUNCTION, fout.write)
    
    header = ['Host: api.findface.pro',
              'Authorization: Token bbpwYV-3rMcIP1-9ZNrgYo9GGqWPG9Zp',
              ]
    
    c.setopt(pycurl.HTTPHEADER, header)
    
    c.setopt(pycurl.POST, 1)
    

    c.setopt(c.HTTPPOST, [
                ("photo1",
                 (c.FORM_FILE, photo1,
                  c.FORM_CONTENTTYPE, "image/png")),
                ("photo2",
                 (c.FORM_FILE, photo2,
                  c.FORM_CONTENTTYPE, "image/png"))])
    
    c.perform()
    resp_code = c.getinfo(pycurl.RESPONSE_CODE)
    resp_data = fout.getvalue().decode('utf-8')

    return [resp_code, resp_data]

import time
start = time.time()
res = face_verify('1.png','1.png')
print(time.time() - start)
