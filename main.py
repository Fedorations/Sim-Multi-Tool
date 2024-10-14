import requests
from colorama import Fore, Style, init
import time
import json
import os
import random
import sys

headers = {
	"x-api-key": "", # put your api key here
	"Accept": "application/json"
}


grabify = "https://grabify.link"
iplogger = "https://iplogger.com"

sep_line = '''
-------------------------------
'''

ascii_art = r'''
                   _, ___, , ,-___,_,  _, ,   
                  (_,' |  |\/|' | / \,/ \,|   
                   _) _|_,| `|  |'\_/'\_/'|__ 
                 '  '    '  `  ' '   '     ' 
                             
'''

print(f"{Fore.LIGHTBLUE_EX}{ascii_art}")

tool_selection = '''
[1] Credit Card Checker           | [5] Roblox Info Fetcher      | [9]
[2] Credit Card Generator         | [6] Discord Webhook Spammer  |
[3] Domain Availability Checker   | [7] Discord Webhook Deleter  |
[4] IP Logger                     | [8] Discord Webhook Message  |
'''
print(f"{Fore.GREEN}{tool_selection}")
time.sleep(1.5)

im = input(f"{Fore.GREEN}Enter Choice (>): ")

if im == '1':
    im_cc = input(f"{Fore.LIGHTBLUE_EX}Card Number (>): ")
    if len(im_cc) < 16:
        print(f"{Fore.RED}Invalid Or Unsupported Region")
    else:
        print(f"{Fore.GREEN}Validating Card")
    if im_cc.isalpha():
        print(f"{Fore.RED}Cant Have Letters!")
        sys.exit()
    else:
        print(f"{Fore.LIGHTBLUE_EX}Recieved Data!")

        req_cc = requests.get(f"https://api.apiverve.com/v1/cardvalidator?number={im_cc}", headers=headers)
        data_cc_check = req_cc.json()
        cc_valid = data_cc_check['data']['isValid']
        cc_ch = data_cc_check['data']['cardNumber']
        print(f"{Fore.LIGHTBLUE_EX}{cc_valid} | {cc_ch}")

if im == '2':
    im_cg = input(f"{Fore.LIGHTBLUE_EX}How Many Cards Do You Want To Generate (>): ")
    if len(im_cg) > 1:
        print(f"{Fore.RED}Too Many | Can't Be Over 10")
    else:
        print(f"{Fore.LIGHTBLUE_EX}Checking / Generating")
        req_scg = requests.get(f"https://api.apiverve.com/v1/cardgenerator?brand=visa&count={im_cg}", headers=headers)
        data_scg_check = req_scg.json()
        cc_val1 = data_scg_check['data']['cards'][0]['number_alt']
        cc_val2 = data_scg_check['data']['cards'][0]['cvv']
        cc_val3 = data_scg_check['data']['cards'][0]['issuer']
        cc_val4 = data_scg_check['data']['owner']['name']
        cc_val5 = data_scg_check['data']['owner']['address']['street']
        cc_val6 = data_scg_check['data']['owner']['address']['zipCode']
        cc_val7 = data_scg_check['data']['cards'][0]['brand']
        print(f"{cc_val1}")
        print(f"{cc_val2}")
        print(f"{cc_val3}")
        print(f"{cc_val4}")
        print(f"{cc_val5}")
        print(f"{cc_val6}")
        print(f"{cc_val7}")
        print(f"{sep_line}")
        print(f"{Fore.RED}MM/YY Not Fetched.")

if im == '3':
    im_cd = input(f"{Fore.RED}.COM Domains Broken | Enter Domain (>): ")
    if len(im_cd) > 20:
        print(f"{Fore.RED}Too Big Of A Domain | Must Be Below 20 Char")
    else:
        print(f"{Fore.LIGHTBLUE_EX}Checking Availability")
        req_cd = requests.get(f"https://api.apiverve.com/v1/domainavailability?domain={im_cd}", headers=headers)
        req_cd_result = req_cd.json()
        req_cd_1 = req_cd_result['data']['available']
        print(f"{req_cd_1}")

if im == '4':
    print(f"{Fore.BLUE}List Of Links Below")
    print(f"{iplogger}")
    print(f"{grabify}")
    time.sleep(5)
    sys.exit()

if im == '5': # this code sourced from other code
    in_id = input("User id (>): ")
    print(f"{Fore.RED}You may wait a minute...")
    time.sleep(5)
    idroblx = requests.get(f"https://users.roblox.com/v1/users/{in_id}") # api
    print(idroblx.text)
    random_ping_times = ("24.6ms", "27.91ms", "54.12ms" "15.11ms" "89.11ms" "1.99ms")
    rdm_choice_ping = random.choice(random_ping_times)
    print(rdm_choice_ping)
 
if im == '6':
    inp_web = input(f"{Fore.BLUE}Enter Webhook To Spam (>): ")
    inp_msg = input(f"{Fore.RED}Enter Message To Spam (>): ")
    for _ in range(9999999999999999999999999):
       spamwebhook = requests.post(inp_web, json={"content": inp_msg})
       if spamwebhook.status_code == 204:
           print(f"{Fore.LIGHTBLUE_EX}(+) Message Sent Successfully | Ping: Not Determined | 100ms")
       else:
           print(f"{Fore.RED}Invalid Webhook")

if im == '7':
    inp_del_web = input("Enter Webhook To Delete (>): ")
    inp_del_start = requests.delete(inp_del_web)
    if inp_del_start.status_code == 204:
        print(f"{Fore.LIGHTBLUE_EX}Deleted!")
        sys.exit
    else:
        print(f"{Fore.RED}Invalid Webhook")

if im == '8':
    inp_send_web = input(f"{Fore.LIGHTBLUE_EX}Enter Webhook (>): ")
    inp_send_web_msg = input(f"{Fore.LIGHTBLUE_EX}Enter Message (>): ")
    web_t_sent = requests.post(inp_send_web, data={"content": inp_send_web_msg})
    if web_t_sent.status_code == 204:
        print("Sent MSG")
    else:
        print(f"{Fore.RED}Invalid Webhook")