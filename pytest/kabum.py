import sys

#Register the Modules folder
sys.path.insert(1, '../../kabumAutomated/')

from uiautomator import device as d
from subprocess import Popen as term
from time import sleep
import Modules.kabumPage as kp
import Modules.kabumData as kd

def basicFluxCartWithLogin(product):
    """Open the app > Log in > Add product to the cart > Open the cart"""
    kp.openKabum()
    kp.login()
    kp.addProduct(product)
    kp.openCart()

def fluxCartWithTwoProducts(productA, productB):
    """Repeat basicFlux to add a product to the cart twice"""
    basicFluxCartWithLogin(productA)
    kp.backToKabumHome()
    basicFluxCartWithLogin(productB)
    sleep(3)
    d(resourceId=kp.resId+'botao_aumentar_qtd', instance=1).click()
    sleep(5)

def finishPurchase(payType):
    """Once inside the cart proceed to the payment process to finish the purchase"""
    kp.addCEP()
    kp.selectPayment(payType)
    kp.insertCardData()

def test_purchaseFlow():
    """
    Part 1 - Purchase flow with 1 item in the cart
    """
    kp.closeKabum()
    kp.cleanCache()
    basicFluxCartWithLogin(kd.product1)
    finishPurchase('credito')
    sleep(2)
    assert d(resourceId=kp.resId+'confirmacao_toolbar').exists == True

def test_purchaseFlow2():
    """
    Part 2 - Purchase flow with 2 items in the cart, the second added with 2 units
    """
    kp.closeKabum()
    kp.cleanCache()
    fluxCartWithTwoProducts(kd.product1, kd.product2)
    thereIsTwo = d(resourceId=kp.resId+'texto_quantidade_produto', text='2').exists
    finishPurchase('credito')
    sleep(2)
    thereIsConfirmation = d(resourceId=kp.resId+'confirmacao_toolbar').exists
    #If there is 2 units added and we were able to reach confirmations screen TC is passed
    assert thereIsTwo == True and thereIsConfirmation == True == True
    
def test_removerDoCarrinho():
    """
    Part 3 - Remove an item from the cart
    """
    kp.closeKabum()
    kp.cleanCache()
    fluxCartWithTwoProducts(kd.product1, kd.product2)
    #Count how many occurencies of remove is being displayed since it's linked to the product
    # it will return exactly the number of products we have in the cart
    total = d(resourceId=kp.resId+'botao_remover').count
    d(resourceId=kp.resId+'botao_remover', instance=0).click()
    sleep(5)
    #Now we just need to verify if the current number of occurencies is lower than at the start
    assert d(resourceId=kp.resId+'botao_remover').count < total
