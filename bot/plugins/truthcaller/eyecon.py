import requests

def eyecon_search(num):
  url = f"https://api.eyecon-app.com/app/getnames.jsp?cli={num}&lang=en&is_callerid=true&is_ic=true&cv=vc_510_vn_4.0.510_a&requestApi=URLconnection&source=MenifaFragment"
  headers = {
      "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; GM1903 Build/QKQ1.190716.003)",
      "Accept": "application/json",
      "Accept-Encoding": "gzip",
      "Connection": "Keep-Alive",
      "e-auth-k": "PgdtSBeR0MumR7fO",
      "e-auth-c": "33",
      "e-auth-v": "e1",
      "e-auth": "3e3495d4-f9c0-4935-80db-35979253968d",
      "content-type": "application/x-www-form-urlencoded",
      "Host": "api.eyecon-app.com"
  }
  response = requests.post(url, headers=headers, timeout=5)
  return response