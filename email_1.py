import imaplib
import base64
import os
import email
import re
import mailparser
from bs4 import BeautifulSoup



pattern_titiel = "You have 1 new tip from"
pattern_titiel_remove = "You have 1 new tip from "
pattern_bet = "Bet: "
pattern_bet_remove =  "\*Bet:\* Each way =E2=80=A2 "
pattern_race_find = "( United Kingdom - | Ireland - )"
pattern_race_remove = "( United Kingdom - | Ireland - )"
sep ="• "

pattern_remove_time =r"[0-9,: ]"

pattern_odd_find ="Odds"
sep_dot = ":"
pattern_stake_find = "Stake"
pattern_book_find = "Bookmaker"


email_user = "betsoley@gmail.com"
email_pass = "peraverda11"

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user, email_pass)
mail.select()
result, data = mail.uid('search', None, "ALL")
# search and return uids instead
i = len(data[0].split()) # data[0] is a space separate string
array_dic = []
for x in range(i):
    latest_email_uid = data[0].split()[x] # unique ids wrt label selected
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # fetch the email body (RFC822) for the given ID
    print("----------------------------")
    id_ = re.sub("[\'b]","",str(latest_email_uid))
    print(id_)
    msg = email.message_from_bytes(email_data[0][1])
    payload = msg.get_payload(decode=True)
    
    for part in msg.walk():
        temp_dic ={}
        if(part.get_content_type() == "text/html"):
            soup = BeautifulSoup(part.get_payload(None, True), "html.parser")
            if(re.match(pattern_titiel,str(soup.title.string))):
                temp_dic["title"]= (re.sub(pattern_titiel_remove,"",soup.title.string))
                temp_dic["email_id"]= id_
                for line in soup.find_all('p'):
                    line = str(line.get_text())
                    if(re.match(pattern_race_find,line)):
                        race = re.sub(pattern_race_remove,"",line)
                        temp_dic["race"]=(race)
                    if(re.search(pattern_bet,line)):
                        bet = line.split(sep, 1)[1]
                        bet = re.sub(" ","",bet)
                        temp_dic["bet"]=(bet)
                    if(re.search(pattern_odd_find,line)):
                        odd = line.split(sep_dot, 1)[1]
                        odd = re.sub(" ","",odd)
                        temp_dic["odd"]=(odd)
                    if(re.search(pattern_stake_find,line)):
                        stake = line.split(sep_dot, 1)[1]
                        stake = re.sub(" ","",stake)
                        stake = re.sub("/10","",stake)
                        temp_dic["stake"]=(stake)
                    if(re.search(pattern_book_find,line)):
                        book = line.split(sep_dot, 1)[1]
                        book = re.sub(" ","",book)
                        temp_dic["book"]=(book)
                array_dic.append(temp_dic)
print(array_dic)
                