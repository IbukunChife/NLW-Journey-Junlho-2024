import requests

payload = {
    "requestor": "yournameorapp",
    "version": "1.0"
}
response = requests.post('https://api.nodemailer.com/user', json=payload)
if response.status_code==200:
    account = response.json()
    print(account)
else:
    raise Exception(f"Could not create Ethereal account:{response.text}")



# {'status': 'success', 
#  'user': 'pk6d3r4nznjvfxpy@ethereal.email', 
#  'pass': '8kg7uar14F1CEutdKc', 
#  'smtp': {'host': 'smtp.ethereal.email', 'port': 587, 'secure': False}, 
#  'imap': {'host': 'imap.ethereal.email', 'port': 993, 'secure': True}, 
#  'pop3': {'host': 'pop3.ethereal.email', 'port': 995, 'secure': True}, 
#  'web': 'https://ethereal.email', 'mxEnabled': False
# }