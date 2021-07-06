import selenium
from selenium import webdriver
import sys
import time

cep = sys.argv[1]

if cep:
    #driver = webdriver.Chrome('.\src\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='.\src\chromedriver.exe', options=options)
    
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')

    #preencher o cep
    elem_cep = driver.find_element_by_name('endereco')
    elem_cep.clear()
    elem_cep.send_keys(cep)

    #escolhe o tipo e pesquisa
    elem_cmb = driver.find_element_by_name('tipoCEP')
    elem_cmb.click()
    driver.find_element_by_xpath('//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]').click()
    driver.find_element_by_id('btn_pesquisar').click()
    time.sleep(1)
    #pegar valores
    logradouro = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]').text
    bairro = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]').text
    localidade = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]').text
    driver.close()
    #
    print("""
    Endereço para o CEP {}:

    Logradouro: {}
    Bairro: {}
    Localidade: {}
    """.format(
        cep,
        logradouro,
        bairro,
        localidade
    ))
#