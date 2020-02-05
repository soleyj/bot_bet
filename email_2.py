import imaplib
import base64
import os
import email
import re
import mailparser

pattern_titiel = "Subject"
pattern_titiel_remove = "Subject: 1 New tip from "
pattern_bet = "Bet:"
pattern_bet_remove =  "\*Bet:\* Each way =E2=80=A2 "
pattern_remove_time =r"[0-9,: ]"
pattern_odd_find ="Odds"
pattern_odd_remove = "\*Odds:\* "
pattern_stake_find = "Stake"
pattern_stake_remove ="\*Stake:\* "
pattern_book_find = "Bookmaker"
pattern_book_remove ="\*Bookmaker:\* "


email_user = "betsoley@gmail.com"
email_pass = "peraverda11"

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user, email_pass)
mail.select()
result, data = mail.uid('search', None, "ALL")
# search and return uids instead
i = len(data[0].split()) # data[0] is a space separate string
for x in range(i):
    latest_email_uid = data[0].split()[x] # unique ids wrt label selected
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # fetch the email body (RFC822) for the given ID
    msg = email.message_from_bytes(email_data[0][1])
    payload = msg.get_payload(decode=True)
    for part in msg.walk():
        if(part.get_content_type() == "text/plain"):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            line = 0
            for index,line in enumerate(part.__str__().splitlines()) :
                print(line)
               
                