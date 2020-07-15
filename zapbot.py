from selenium import webdriver
import time 

class WhatsappBot:
    def __init__(self):
        self.mensagem = "OLÁ, ESSA MENSAGEM É UM TESTE, FAVOR NÃO RESPONDER!!!"
        self.grupo = ["Teste"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMendagens(self):
        #<span dir="auto" title="Teste" class="_1wjpf _3NFp9 _3FXB1">Teste</span>  
        #<div tabindex="-1" class="_1Plpp">
        #<span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupo:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMendagens()