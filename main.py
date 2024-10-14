import requests
from colorama import Fore, Style, init
import time
import string
import json
import os
import random
import sys
import qrcode
from PIL import Image, ImageDraw

headers = {
	"x-api-key": "your sigma api key", # put your api key here
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
                      [DONATE] Support Me :)

[1] Credit Card Checker           | [5] Roblox Info Fetcher      | [09]
[2] Credit Card Generator         | [6] Discord Webhook Spammer  | [10]
[3] Domain Availability Checker   | [7] Discord Webhook Deleter  | [11] 
[4] IP Logger                     | [8] Discord Webhook Message  | [12]
'''
print(f"{Fore.LIGHTBLUE_EX}{tool_selection}")
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
        time.sleep(4)

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

if im == 'donate':
    print(f"{Fore.LIGHTBLUE_EX}crypto | cashapp | paypal")
    payment_method = input(f"{Fore.YELLOW}What Payment Method (>): ")
    if payment_method == 'crypto':
        print(f"{Fore.LIGHTBLUE_EX}BTC: bc1qk4hgud574043v63g7t6cmmqgw95vjklvkjtjcy")
        print(f"{Fore.LIGHTBLUE_EX}ETH: 0x99DF6163Ea3BCCF9966d1c108b5771cd4f6A8928")
        print(f"{Fore.LIGHTBLUE_EX}LTC: La6DTC5Y9dcRLRZEiDuoXctxe2ziPTEAfV")
        print(f"{Fore.LIGHTBLUE_EX}XMR: 83qgo5cmAeciHA3BvqkB7abMn8eyRpnA5HuKXqqnGoFUZFkeWSGZSdaHkygkLxJW97EaK9QMu5Xq4EUe3REwwDcMB3vaRuP")
        print(f"{Fore.RED}for others dm @spo.t - discord")
        input("enter to exit.")

    if payment_method == 'cashapp':
        print(f"{Fore.YELLOW}$waterrblx | on cashapp")
        input("enter to exit.")

    if payment_method == 'paypal':
        print(f"{Fore.GREEN}laughuntilretire@gmail.com | paypal email")
        input("enter to exit.")

if im == '9':
    print("in beta!")
