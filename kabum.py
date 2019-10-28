from uiautomator import device as d
from subprocess import Popen as term
from time import sleep
import kabumPage

produto1 = 'SA400S37'
produto2 = 'YD1600BBAEBOX'

def test_fluxoCompra():
    """
    Parte 1 - Fluxo de compra com 1 item
    """
    kabumPage.fecharKabum()
    kabumPage.limparCache()
    kabumPage.fluxoBasicoCarrinhoComLogin(produto1)
    kabumPage.finalizarCompra('credito')
    sleep(2)
    assert d(resourceId='br.com.kabum.webviewapp:id/confirmacao_toolbar').exists == True

def test_fluxoCompra2():
    """
    Parte 2 - Fluxo de compra com 2 itens, um deles com 2 unidades
    """
    kabumPage.fecharKabum()
    kabumPage.limparCache()
    kabumPage.fluxoCarrinhoComDoisProdutos(produto1, produto2)
    tem2 = d(resourceId='br.com.kabum.webviewapp:id/texto_quantidade_produto', text='2').exists
    kabumPage.finalizarCompra('credito')
    sleep(2)
    temConfirma = d(resourceId='br.com.kabum.webviewapp:id/confirmacao_toolbar').exists
    assert tem2 == True and temConfirma == True == True
    
def test_removerDoCarrinho():
    """
    Parte 3 - Remover um item do carrinho
    """
    kabumPage.fecharKabum()
    kabumPage.limparCache()
    kabumPage.fluxoCarrinhoComDoisProdutos(produto1, produto2)
    total = d(resourceId="br.com.kabum.webviewapp:id/botao_remover").count
    d(resourceId='br.com.kabum.webviewapp:id/botao_remover', instance=0).click()
    sleep(5)
    assert d(text="br.com.kabum.webviewapp:id/botao_remover").count < total