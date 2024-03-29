from uiautomator import device as d
from subprocess import Popen as term
from time import sleep
from Modules import kabumData as kd

#Main Activity
resId = 'br.com.kabum.webviewapp:id/'

#ImplicityWait
waitLimit = 5000

def openKabum():
    term('adb shell am start -n br.com.kabum.webviewapp/br.com.kabum.kabumstore.activity.SplashScreen', shell=True).wait()
    print('\nStarting app')

def cleanCache():
    #Useful to clear the search history and the logged user to start a new scenario from state zero
    term('adb shell pm clear br.com.kabum.webviewapp', shell=True).wait()
    print('\nCache cleaned')

def closeKabum():
    term('adb shell am force-stop br.com.kabum.webviewapp',shell=True).wait()
    print('\nClosing app')

def login():
    d(resourceId=resId+'mais').click()
    if d(resourceId=resId+'botao_entrar').exists == True:
        print('\nStarting Login')
        d(resourceId=resId+'texto_login_email').set_text(kd.user)
        d(resourceId=resId+'texto_password').set_text(kd.pwd)
        d(resourceId=resId+'botao_entrar').click()
        print('Login done')
    else:
        print('\nAlready logged in')
        pass

def searchProduct(productName):
    print('\nSearching product')

    if d(resourceId=resId+'search_menu').exists == False:
        d(resourceId=resId+'searchWidget').click()
    else:
        d(resourceId=resId+'search_menu').click()

    d(resourceId=resId+'search_src_text').wait.exists(timeout=waitLimit)
    d(resourceId=resId+'search_src_text').set_text(productName)
    d.press.enter()
    d.wait.idle()
    print('Search finished')

def addProduct(productName):
    searchProduct(productName)
    print('\nAdding product to the cart')
    #Open product page
    d(resourceId=resId+'card_view_favoritos')[0].click()
    #Add product on the cart
    d(resourceId=resId+'floating_carrinho').click()
    print('Product added')

def openCart():
    print('\nOpening cart')
    d(resourceId=resId+'carrinho_menu').click()
    print('Cart opened')

def addCEP():
    print('\nInserting CEP')
    # Insert CEP
    if d(resourceId=resId+'edit_text_cep').exists == True:
        d(resourceId=resId+'edit_text_cep').set_text(kd.cep)
        d.wait.idle()       
        d(scrollable=True).scroll.to(resourceId=resId+'botao_finalizar_bottom')
        d(resourceId=resId+'botao_finalizar_bottom').click()
    else:
        # sleep(2)
        d.wait.update()       
        d(scrollable=True).scroll.to(resourceId=resId+'botao_finalizar_bottom')
        d(resourceId=resId+'botao_finalizar_bottom').click()
    print('CEP inserted')

def selectPayment(payType):
    if payType == 'credito':
        d(text='CARTÃO DE CRÉDITO').click()
    elif payType == 'boleto':
        d(text='BOLETO BANCÁRIO').click()

def insertCardData():
    print('\nInsert CC info')
    sleep(2)
    d(resourceId=resId+'texto_numero_cartao').set_text(kd.creditNumber)
    d.press.back()
    d(resourceId=resId+'texto_nome_cartao').set_text(kd.fakeName)
    d.press.back()
    d(resourceId=resId+'texto_validade_cartao').set_text(kd.creditDate)
    d.press.back()
    d(resourceId=resId+'texto_codigo_cartao').set_text(kd.creditCVV)
    d.press.back()
    d(resourceId=resId+'texto_cpf_cartao').set_text(kd.fakeCpf)
    d.press.back()
    d(resourceId=resId+'texto_nascimento_cartao').set_text(kd.fakeBirthday)
    d.press.back()
    d(scrollable=True).scroll.to(resourceId=resId+'botao_cartao')
    d(resourceId=resId+'botao_cartao').click()
    print('Credit card info inserted')

def backToKabumHome():
    while d(resourceId=resId+'bb_bottom_bar_item_container').exists == False:
        print("Pressed back")
        d.press.back()