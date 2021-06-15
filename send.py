import requests
def send_sms():
    number = input("mobile number:")


    messages = input("enter message what you want to send:")

    url = "https://www.fast2sms.com/dev/bulkV2"

    api = "oTcGsr5n4JLyR6e0W83qaPvzuYlHEbhdptNVjwZmM2OUDxAQfF60ej8qmz1XGacd2"  #importent   :: this api key is not workig for api key 
    #please login into fast2sms and you will gwt api key and copy and paste.
    querystring = {
        "authorization":api,
        "sender_id": " TXTIND",#this is also you will get in fast 2 sms 
        "message": messages,
        "language": "english",
        "route": "v3",#this is also you will get in fast 2 sms 
        "numbers": number
    }

    headers = {
        'cache-control': "no-cache"
    }

    requests.request("GET", url, headers=headers, params=querystring)
send_sms()
