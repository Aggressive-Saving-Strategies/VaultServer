import bottle
from vaultserver import api
from vaultserver import consts

@bottle.get('/account/credits')
def credits():
    return api.get_credits(consts.primary_account)

@bottle.post('/account/lose')
def lose():
    lost = bottle.request.json['amount']
    return api.move(consts.primary_account, consts.savings_account, lost)

@bottle.post('/account/win')
def win():
    won = bottle.request.json['amount']
    return api.move(consts.savings_account, consts.primary_account, won)

bottle.run(debug=True, reloader=True, port=8080, host='0.0.0.0')
