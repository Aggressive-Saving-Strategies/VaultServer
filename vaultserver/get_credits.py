def get_credit_vault():
    #Mr Bergen specific
    #Vault account balance
    ACCOUNT_ID = "af959f0f-f43e-4c9b-a899-47d4478f0640"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb25zZW50SWQiOiJhNDE4YTA3OS1hNjBiLTQ5NDAtOTI5My05OTUwM2U0YWNmM2UiLCJpYXQiOjE1NzM5MTc4NTh9.Xkyq6EyVIZq05H0bOEbOpbp2wEfLSj3EKA-DWz3N2qE"
    URL = "https://developers.danskebank.com/_/virtualbank-api/aisp/v3.1/accounts/"+ACCOUNT_ID+"/balances"

    HEADERS = {"Authorization":token}

    r = requests.get(url=URL, headers=HEADERS)
    amount = r.json()["Data"]["Balance"][0]["Amount"]["Amount"]
    return amount

def get_credit_account():
    #Mr Bergen specific
    #Vault account balance
    ACCOUNT_ID = "0ea531ae-e3e8-4b04-8d95-ab66407fba29"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb25zZW50SWQiOiI1MTY5M2JhMy1iMTQyLTRiMTctYTcxMC0wNjc2NjlkNTQ1NjkiLCJpYXQiOjE1NzM5MTI1OTd9.1MpBF78qDf5Mhk6kF5_YsSsCJi-9p-EAAxcX2DolwwE"
    URL = "https://developers.danskebank.com/_/virtualbank-api/aisp/v3.1/accounts/"+ACCOUNT_ID+"/balances"

    HEADERS = {"Authorization":token}

    r = requests.get(url=URL, headers=HEADERS)
    amount = r.json()["Data"]["Balance"][0]["Amount"]["Amount"]
    return amount

get_credit_vault()
get_credit_account()
