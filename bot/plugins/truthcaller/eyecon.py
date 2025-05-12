import requests
import os

def eyecon_search(num):
  url = f"https://api.eyecon-app.com/app/getnames.jsp?cli={num}&&lang=en&is_callerid=true&is_ic=false&cv=vc_542_vn_4.0.542_a&requestApi=URLconnection&source=RegistrationGetMyName"
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
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
