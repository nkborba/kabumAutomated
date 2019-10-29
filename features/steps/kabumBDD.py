from behave import *
from uiautomator import device as d
import kabumPage as kp
from time import sleep

total = 0

@given('the Kabum Store')
def step_impl(context):
    kp.closeKabum()
    kp.cleanCache()
    kp.openKabum()

@when('we log in')
def step_impl(context):
    kp.login()

@when('we add the product "{product}" to the cart')
def step_impl(context, product):
    kp.addProduct(product)

@when('we open the cart')
def step_impl(context):
    kp.openCart()

@when('we add CEP')
def step_impl(context):
    kp.addCEP()

@when('we add select payment type as "{payType}"')
def step_impl(context, payType):
    kp.selectPayment(payType)

@when('we insert credit card info')
def step_impl(context):
    kp.insertCardData()

@when('we add another product "{product}" to the cart')
def step_impl(context, product):
    kp.backToKabumHome()
    kp.addProduct(product)

@when('we add an unit of the last product')
def step_impl(context):
    sleep(3)
    d(resourceId=kp.resId+'botao_aumentar_qtd', instance=1).click()
    sleep(5)

@when('we count items inside the cart')
def step_impl(context):
    sleep(5)
    global total
    total = d(resourceId=kp.resId+'botao_remover').count
    sleep(2)

@when('we delete an item')
def step_impl(context):
    d(resourceId=kp.resId+'botao_remover', instance=0).click()

@then('there is fewer items in the cart')
def step_impl(context):
    num = d(resourceId=kp.resId+'botao_remover').count
    sleep(2)
    assert (num < total) == True

@then('we finish the purchase')
def step_impl(context):
    sleep(3)
    assert d(resourceId=kp.resId+'confirmacao_toolbar').exists == True
    sleep(3)