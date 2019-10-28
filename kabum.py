from uiautomator import device as d
from subprocess import Popen as term
from time import sleep

produto1 = 'SA400S37'
produto2 = 'YD1600BBAEBOX'
cep = '13086-510'
fakeName = 'Contrata o Nicholas'
fakeCpf = '708.005.230-08'
fakeBirthday = '28/04/1992'
user = 'nbtests01@gmail.com'
pwd = 'tester1234'

#All credit card information was generated on https://www.4devs.com.br/gerador_de_numero_cartao_credito and are not real
creditNumber = '5476 1402 7281 7022'
creditDate = '28/21'
creditCVV = '582'

def abrirKabum():
    term('adb shell am start -n br.com.kabum.webviewapp/br.com.kabum.kabumstore.activity.SplashScreen', shell=True).wait()
    print('\nStarting app')

def limparCache():
    #Useful to clear the search history and the logged user to start a new scenario from state zero
    term('adb shell pm clear br.com.kabum.webviewapp', shell=True).wait()
    print('\nCache cleaned')

def fecharKabum():
    term('adb shell am force-stop br.com.kabum.webviewapp',shell=True).wait()
    print('\nClosing app')

def fazerLogin():
    # (openKabum(), 'soSegue')[d(packageName='br.com.kabum.webviewapp').exists]
    d(resourceId='br.com.kabum.webviewapp:id/mais').click()
    if d(resourceId='br.com.kabum.webviewapp:id/botao_entrar').exists == True:
        print('\nStarting Login')
        d(resourceId='br.com.kabum.webviewapp:id/texto_login_email').set_text(user)
        d(resourceId='br.com.kabum.webviewapp:id/texto_password').set_text(pwd)
        d(resourceId='br.com.kabum.webviewapp:id/botao_entrar').click()
        print('Login done')
    else:
        print('\nAlready logged in')
        pass

def pesquisaProduto(nomeProduto):
    print('\nSearching product')

    if d(resourceId='br.com.kabum.webviewapp:id/search_menu').exists == False:
        d(resourceId='br.com.kabum.webviewapp:id/searchWidget').click()
    else:
        d(resourceId='br.com.kabum.webviewapp:id/search_menu').click()

    d(resourceId='br.com.kabum.webviewapp:id/search_src_text').set_text(nomeProduto)
    d.press.enter()
    sleep(3)
    print('Search finished')

def adicionaProduto(nomeProduto):
    pesquisaProduto(nomeProduto)
    print('\nAdding product to the cart')
    #Abre o produto
    d(resourceId='br.com.kabum.webviewapp:id/card_view_favoritos')[0].click()
    #Adiciona no carrinho
    d(resourceId='br.com.kabum.webviewapp:id/floating_carrinho').click()
    print('Product added')

def abrirCarrinho():
    print('\nOpening cart')
    d(resourceId='br.com.kabum.webviewapp:id/carrinho_menu').click()
    print('Cart opened')

def adicionaCEP():
    print('\nInserting CEP')
    # Insere CEP
    if d(resourceId='br.com.kabum.webviewapp:id/edit_text_cep').exists == True:
        d(resourceId='br.com.kabum.webviewapp:id/edit_text_cep').set_text(cep)
    else:        
        d(scrollable=True).scroll.to(resourceId='br.com.kabum.webviewapp:id/botao_finalizar_bottom')
        d(resourceId='br.com.kabum.webviewapp:id/botao_finalizar_bottom').click()
    print('CEP inserted')

def selecionaPagamento(forma):
    if forma == 'credito':
        d(text='CARTÃO DE CRÉDITO').click()
    elif forma == 'boleto':
        d(text='BOLETO BANCÁRIO').click()

def inserirDadosCartao():
    print('\nInsert CC info')
    sleep(2)
    d(resourceId='br.com.kabum.webviewapp:id/texto_numero_cartao').set_text(creditNumber)
    d.press.back()
    d(resourceId='br.com.kabum.webviewapp:id/texto_nome_cartao').set_text(fakeName)
    d.press.back()
    d(resourceId='br.com.kabum.webviewapp:id/texto_validade_cartao').set_text(creditDate)
    d.press.back()
    d(resourceId='br.com.kabum.webviewapp:id/texto_codigo_cartao').set_text(creditCVV)
    d.press.back()
    d(resourceId='br.com.kabum.webviewapp:id/texto_cpf_cartao').set_text(fakeCpf)
    d.press.back()
    d(resourceId='br.com.kabum.webviewapp:id/texto_nascimento_cartao').set_text(fakeBirthday)
    d.press.back()
    d(resourceId='br.com.kabum.webviewapp:id/botao_cartao').click()
    print('Credid card info inserted')

def voltarHomeKabum():
    while d(resourceId='br.com.kabum.webviewapp:id/home').exists == False:
        d.press.back()

def fluxoBasicoCarrinhoComLogin(produto):
    abrirKabum()
    fazerLogin()
    adicionaProduto(produto)
    abrirCarrinho()

def fluxoCarrinhoComDoisProdutos(produtoA, produtoB):
    fluxoBasicoCarrinhoComLogin(produtoA)
    voltarHomeKabum()
    fluxoBasicoCarrinhoComLogin(produtoB)
    sleep(3)
    d(resourceId='br.com.kabum.webviewapp:id/botao_aumentar_qtd', instance=1).click()
    sleep(5)

def finalizarCompra(pagamento):
    adicionaCEP()
    selecionaPagamento(pagamento)
    inserirDadosCartao()

def test_fluxoCompra():
    """
    Parte 1 - Fluxo de compra com 1 item
    """
    fecharKabum()
    limparCache()
    fluxoBasicoCarrinhoComLogin(produto1)
    finalizarCompra('credito')
    assert d(resourceId='br.com.kabum.webviewapp:id/confirmacao_toolbar').exists == True

def test_fluxoCompra2():
    """
    Parte 2 - Fluxo de compra com 2 itens, um deles com 2 unidades
    """
    fecharKabum()
    limparCache()
    fluxoCarrinhoComDoisProdutos(produto1, produto2)
    print('\n##### Product 2 inserted with 2 units #####')
    tem2 = d(resourceId='br.com.kabum.webviewapp:id/texto_quantidade_produto', text='2').exists
    finalizarCompra('credito')
    temConfirma = d(resourceId='br.com.kabum.webviewapp:id/confirmacao_toolbar').exists
    assert tem2 == True and temConfirma == True
    

def test_removerDoCarrinho():
    """
    Parte 3 - Remover um item do carrinho
    """
    fecharKabum()
    limparCache()
    fluxoCarrinhoComDoisProdutos(produto1, produto2)
    total = d(resourceId="br.com.kabum.webviewapp:id/botao_remover").count
    d(resourceId='br.com.kabum.webviewapp:id/botao_remover', instance=0).click()
    sleep(5)
    assert d(text="br.com.kabum.webviewapp:id/botao_remover").count < total

# test_fluxoCompra()
# test_fluxoCompra2()
# test_removerDoCarrinho()

# fecharKabum()
# limparCache()