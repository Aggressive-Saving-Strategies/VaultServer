import bottle
from vaultserver import api
from vaultserver import consts
import requests

@bottle.get('/account/credits')
def credits():
    return api.get_credits(consts.primary_account)

@bottle.post('/account/lose')
def lose():
    lost = bottle.request.json['amount']
    amount = lost
    PLAYGROUND_ID = "02adf7f0-1a1a-4865-9197-7712c1839e80"

    #This works only for Bergen, the customer and merchant id's are his
    URL = "https://developers.danskebank.com/_/playground-api/v1.0/auth"

    #Not customer specific
    ClientId = "b7b03ios2ell6l25mxmdarighzb0lgtm"
    Secret = "q2iwpffwogp4hdzk4ib7e29rywxnhlc1"

    PARAMS = {'ClientId': ClientId,
              'Secret': Secret}

    r = requests.post(url=URL, data=PARAMS)

    token = r.json()["accessToken"]

    #Mr Bergen specific
    #Take from use account
    CUSTOMER_ID = "631ccfb5-ce89-42f5-b003-68d04acc4228"
    ACCOUNT_ID = "0ea531ae-e3e8-4b04-8d95-ab66407fba29"

    URL = "https://developers.danskebank.com/_/playground-api/v1.0/"+PLAYGROUND_ID+"/customer/"+CUSTOMER_ID+"/account/"+ACCOUNT_ID+"/transaction"
    accessToken = token

    HEADERS = {"Authorization":"Bearer "+accessToken}

    PARAMS = {"template":"debit", "amount":amount}
    r = requests.post(url=URL, headers=HEADERS, data=PARAMS)

    #Mr Bergen specific
    #Add to Vault account
    CUSTOMER_ID = "f539af5b-0a51-4d12-beae-5bba67ce1408"
    ACCOUNT_ID = "af959f0f-f43e-4c9b-a899-47d4478f0640"

    URL = "https://developers.danskebank.com/_/playground-api/v1.0/"+PLAYGROUND_ID+"/customer/"+CUSTOMER_ID+"/account/"+ACCOUNT_ID+"/transaction"
    accessToken = token

    HEADERS = {"Authorization":"Bearer "+accessToken}

    PARAMS = {"template":"credit", "amount":amount}
    r = requests.post(url=URL, headers=HEADERS, data=PARAMS)

@bottle.post('/account/win')
def win():
    won = bottle.request.json['amount']
    
    amount = won
    
    PLAYGROUND_ID = "02adf7f0-1a1a-4865-9197-7712c1839e80"

    #This works only for Bergen, the customer and merchant id's are his
    URL = "https://developers.danskebank.com/_/playground-api/v1.0/auth"

    #Not customer specific
    ClientId = "b7b03ios2ell6l25mxmdarighzb0lgtm"
    Secret = "q2iwpffwogp4hdzk4ib7e29rywxnhlc1"

    PARAMS = {'ClientId': ClientId,
              'Secret': Secret}

    r = requests.post(url=URL, data=PARAMS)

    token = r.json()["accessToken"]

    #Mr Bergen specific
    #Give to use account
    CUSTOMER_ID = "631ccfb5-ce89-42f5-b003-68d04acc4228"
    ACCOUNT_ID = "0ea531ae-e3e8-4b04-8d95-ab66407fba29"

    URL = "https://developers.danskebank.com/_/playground-api/v1.0/"+PLAYGROUND_ID+"/customer/"+CUSTOMER_ID+"/account/"+ACCOUNT_ID+"/transaction"
    accessToken = token

    HEADERS = {"Authorization":"Bearer "+accessToken}

    PARAMS = {"template":"credit", "amount":amount}
    r = requests.post(url=URL, headers=HEADERS, data=PARAMS)

    #Mr Bergen specific
    #Take from Vault account
    CUSTOMER_ID = "f539af5b-0a51-4d12-beae-5bba67ce1408"
    ACCOUNT_ID = "af959f0f-f43e-4c9b-a899-47d4478f0640"

    URL = "https://developers.danskebank.com/_/playground-api/v1.0/"+PLAYGROUND_ID+"/customer/"+CUSTOMER_ID+"/account/"+ACCOUNT_ID+"/transaction"
    accessToken = token

    HEADERS = {"Authorization":"Bearer "+accessToken}

    PARAMS = {"template":"debit", "amount":amount}
    r = requests.post(url=URL, headers=HEADERS, data=PARAMS)

bottle.run(debug=True, reloader=True, port=8080, host='0.0.0.0')
