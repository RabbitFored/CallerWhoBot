import requests
import os

def eyecon_search(num):
  url = f"https://api.eyecon-app.com/app/getnames.jsp?cli={num}&lang=en&is_callerid=true&is_ic=true&cv=vc_510_vn_4.0.510_a&requestApi=URLconnection&source=MenifaFragment"
  headers = {
      "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; GM1903 Build/QKQ1.190716.003)",
      "Accept": "application/json",
      "Accept-Encoding": "gzip",
      "Connection": "Keep-Alive",
      "e-auth-k": os.environ['e-auth-k'],
      "e-auth-c": os.environ['e-auth-c'],
      "e-auth-v": os.environ['e-auth-v'],
      "e-auth": os.environ['e-auth'],
      "content-type": "application/x-www-form-urlencoded",
      "Host": "api.eyecon-app.com"
  }
  response = requests.post(url, headers=headers, timeout=5)
  return response
