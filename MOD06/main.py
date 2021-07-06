#%%
#Importando pacote do selenium
from selenium import webdriver
import time
# %%
#carregando o driver e acessando o site da HOW
driver = webdriver.Chrome('.\src\chromedriver.exe')

# %%
#Acesso ao site da HOW
#Clicando em elementos do site
driver.get('https://howedu.com.br')
driver.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[2]/div[1]').click()
driver.find_element_by_xpath('/html/body/section[4]/div/div/div[2]/a').click()
# %%
#Acesso a site dos correios
driver = webdriver.Chrome('.\src\chromedriver.exe')
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')

#preencher o cep
elem_cep = driver.find_element_by_name('endereco')
elem_cep.clear()
elem_cep.send_keys('59086005')

#escolhe o tipo e pesquisa
elem_cmb = driver.find_element_by_name('tipoCEP')
elem_cmb.click()
elem_tipo = driver.find_element_by_xpath('//*[@id="formulario"]/div[2]/div/div[2]/select/option[6]').click()
driver.find_element_by_name('btn_pesquisar').click()
time.sleep(5)
logradouro = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[1]').text
bairro = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[2]').text
localidade = driver.find_element_by_xpath('/html/body/main/form/div[1]/div[2]/div/div[3]/table/tbody/tr/td[3]').text

# %%
print("""
Endereço: {}
Bairro: {}
Localidade: {}
""".format(
    logradouro,
    bairro,
    localidade
))
# %%
driver.close()
# %%
