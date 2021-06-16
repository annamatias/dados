from urllib.request import urlopen #biblioteca de requests em sites
from urllib.error import HTTPError #trata a exceção de erros genericos
from urllib.error import URLError #captura erros detalhados e que não pode ser visto no generico
from bs4 import BeautifulSoup #essa biblioteca ela formata qualquer html ou xml que foi mal formatado ou confuso (tratamento) 
import time 

#html = urlopen('https://pensiee.blogspot.com/p/sobre-o-pensiee.html')
#print(html.read())
#bs = BeautifulSoup(html.read(), 'html.parser')
#print(bs.h1)

nome_arquivo = 'log_request.txt'
tempo = time.ctime()

#tratamento de erros com registro de log
#melhoria: fazer função do registro de log
def Logger(nome_arquivo, path, status):
    if nome_arquivo == "log_request.txt":
        log = open(path, 'ra+')
        log.writelines(str(bs.h1))
        log.writelines(f" \n================= \ntime of request: {tempo} \n{status} \n================= \n")
    log.close()
    return "request has log"

try:
    url = urlopen('https://pensiee.blogspot.com/p/sobre-o-pensiee.html')
    bs = BeautifulSoup(url.read(), 'html.parser')
except HTTPError as error:
    try:
        if nome_arquivo == 'log_request.txt':
            log = open('home/anna.santos/Documentos/karol/dados/data_engineer/web_scraping/log_request.txt', 'r+')
            log.writelines(str(error))
    except FileNotFoundError:
        log = open(nome_arquivo, 'a')
        log.writelines(str(error))
        log.writelines(f" \ntime of request: {tempo} \n================= \n")
    log.close()
    print(error)
except URLError as error:
    try:
        if nome_arquivo == 'log_request.txt':
            log = open('home/anna.santos/Documentos/karol/dados/data_engineer/web_scraping/log_request.txt', 'r+')
            log.writelines("It's not be found")
    except FileNotFoundError:
        log = open(nome_arquivo, 'a')
        log.writelines(f" \n================= \ntime of request: {tempo} \n================= \n")
    log.close()
    print("It's not be found")
else:
    try:
        if nome_arquivo == 'log_request.txt':
            log = open('home/anna.santos/Documentos/karol/dados/data_engineer/web_scraping/log_request.txt', 'r+')
            log.writelines(str(bs.h1))
    except FileNotFoundError:
        Logger(nome_arquivo, 'home/anna.santos/Documentos/karol/dados/data_engineer/web_scraping/log_request.txt','request of success')
    print('Requisição ta funfando')


