import sys

#Register the Modules folder
sys.path.insert(1, '../../../kabumAutomated/')

from behave import *
from uiautomator import device as d
from Modules import kabumPage as kp
from time import sleep

total = 0

@given('the Kabum Store')
def step_impl(context):
    kp.closeKabum()
    kp.cleanCache()
    kp.openKabum()

@when('I log in')
def step_impl(context):
    kp.login()

@when('I add the product to the cart')
def step_impl(context):
    for row in context.table:
        p = row['product']
        kp.backToKabumHome()
        kp.addProduct(p)

@when('I open the cart')
def step_impl(context):
    kp.openCart()

@when('I add CEP')
def step_impl(context):
    kp.addCEP()

@when('I add select payment type as "{payType}"')
def step_impl(context, payType):
    kp.selectPayment(payType)

@when('I insert credit card info')
def step_impl(context):
    kp.insertCardData()

@when('I add an unit of the last product')
def step_impl(context):
    sleep(5)
    d(resourceId=kp.resId+'botao_aumentar_qtd', instance=1).click()

@when('I count items inside the cart')
def step_impl(context):
    sleep(5)
    global total
    total = d(resourceId=kp.resId+'botao_remover').count
    sleep(2)

@when('I delete an item')
def step_impl(context):
    d(resourceId=kp.resId+'botao_remover', instance=0).click()

@then('I see fewer items in the cart')
def step_impl(context):
    num = d(resourceId=kp.resId+'botao_remover').count
    sleep(2)
    assert (num < total) == True

@then('I should finish the purchase sucessfully')
def step_impl(context):
    sleep(3)
    assert d(resourceId=kp.resId+'confirmacao_toolbar').exists == True
    sleep(3)