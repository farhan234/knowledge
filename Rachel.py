import os
import smtplib
from twilio.rest import Client


def main():
    # Account SID from console
    account_sid_one = "ACf523bbdc454c6639a9e324c66a05d68b"

    # Auth Token from console
    auth_token_one = "1bd576083cc3dc1f4a75361c4b294a5d"

    account_sid = os.environ.get('TWILIO_ACCOUNT_SIDE')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid_one, auth_token_one)

    # run func2 to return the lyric list
    lyric_list = func2()

    # run func1 to create the twilio app login

    for i in range(len(lyric_list)):
        print(lyric_list[i])

    message = client.messages.create(
        to="‭+12143150137‬",
        from_="+12569603631",
        body="suck my asss")


# Function to read file line by line
def func2():
    lyric_list = []
    with open('/Users/farhanali/Documents/Rachel.txt', 'r') as song:
        # reading each line
        for line in song:
            # strip the line
            stripped_line = line.strip()
            line_list = stripped_line.split()
            lyric_list.append(line_list)
    song.close()
    return lyric_list


def main():

    print(message.sid)
main()
