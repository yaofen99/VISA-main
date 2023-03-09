import requests

def send_to_telegram(message):

    apiToken = '6194281790:AAFyDI-ggKlaNSFbASmNbHG6TmjJ7lkmW_8'
    chatID = '-1001756342015'

    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("success!")
