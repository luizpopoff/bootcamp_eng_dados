#%%
# imports
import requests
import json

# %%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url)

# %%
if ret:
    print(ret)
else:
    print('Falhou')
# %%
dolar = json.loads(ret.text)['USDBRL']

# %%
dolar['bid']

# %%
print(f"$20 é igual a R${float(dolar['bid']) * 20 :.2f}.")
# %%

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'

    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor :.2f} {moeda[-3:]}.")

# %%
#Usando o Try para tratar erro
try:
    cotacao(20, 'JPY-BRL')
except:
    pass
# %%
try:
    cotacao(20, 'Y-BRL')
except Exception as e:
    print(e)
else:
    print('OK')
# %%
def multi_moeda(valor):
    lst_money = [
        "USD-BRL",
        "EUR-BRL",
        "BTC-BRL",
        "RPL-BRL",
        "JPY-BRL"
    ]

    for moeda in lst_money:
        url = f'https://economia.awesomeapi.com.br/last/{moeda}'

        ret = requests.get(url)
        dolar = json.loads(ret.text)[moeda.replace('-','')]
        print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor :.2f} {moeda[-3:]}.")
        
# %%
multi_moeda(20)
# %%
#usando decorador
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f'{func.__name__} falhou')
    return inner_func


@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'

    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor :.2f} {moeda[-3:]}.")

# %%

multi_moeda(20,'USD-BRL')
multi_moeda(20,'EUR-BRL')
multi_moeda(20,'BTC-BRL')
multi_moeda(20,'RPL-BRL')
multi_moeda(20,'JPY-BRL')


# %%
#Usando a biblioteca backoff para tratar o erro e fazer tentativas

import backoff
import random

@backoff.on_exception(backoff.expo, (ConnectionAbortedError,ConnectionRefusedError,TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "Ok!"
# %%
test_func()
# %%
test_func(42)
# %%
test_func(42, 51, nome='Luiz')
# %%

import logging
# %%

log = logging.getLogger()
log.setLevel(logging.DEBUG)
formater = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formater)
log.addHandler(ch)

# %%

@backoff.on_exception(backoff.expo, (ConnectionAbortedError,ConnectionRefusedError,TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f"RND: {rnd}")
    log.info(f"args: {args if args else 'sem args'}")
    log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "Ok!"
# %%
test_func()
# %%
