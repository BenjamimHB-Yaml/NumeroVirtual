import requests
import re

url = "https://sms-verification-number.com/api/getMessageList/?countryCodeApi=portugal&number=351911813721&page=1&lang=en"

headers = {
      "User-Agent": "Mozilla/5.0",
      "Accept": "application/json",
      "Referer": "https://sms-verification-number.com/free-numbers-en/",
      "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=headers)
data = r.json()

html = data["html"]

# pegar serviços
services = re.findall(r'monitor-item__heading.*?>(.*?)<', html)

# pegar mensagens
messages = re.findall(r'monitor-item__text">\s*(.*?)\s*</p>', html, re.DOTALL)

# pegar códigos
codes = re.findall(r'\b\d{4,8}\b', html)

for i in range(min(len(services), len(messages), len(codes))):
      print("Serviço:", services[i].strip())
      print("Mensagem:", messages[i].strip())
      print("-----")
      print("numero de telefone virtual +351 911 813 721")
