import requests as r
dolar = r.get('https://economia.awesomeapi.com.br/json/last/USD-BRL', auth=('user', 'pass'))
res = dolar.json()
print("******************************************")
print("O dolar agora está " + res["USDBRL"]["bid"])
print("A maxima do dia foi: " + res["USDBRL"]["high"])
print("A minima do dia foi: " + res["USDBRL"]["low"])
print("******************************************")
