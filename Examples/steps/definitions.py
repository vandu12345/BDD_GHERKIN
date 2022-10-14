
from behave import given, then, when



@given("I have a new {item} in my cart")
def i_have_item_in_cart(context, item):

    print("The item is: {}".format(item))

@when('I click on {button_to_click}')
def click_button(context, button_to_click):

    print("I am clicking the button: {}".format(button_to_click))

@then('I should see "{txt}"')
def i_should_see_text(context, txt):

    if txt not in ['success', 'error']:
        raise Exception("Unexpected text passed in.")

    if txt.lower() == 'success':
        print("Yeyyyyyyy")
    else:
        print("NOOOOOOOOOO")
    print("Checking if I see the '{}' text".format(txt))
    print("PASS. I see the '{}' text".format(txt))

@given('I start a call with "{qty}" participants')
def add_multiple_participants(context, qty):

    print("The number of participants is: {}".format(qty))

    print('####################')
    print (type(qty))
    new_qty = int(qty)
    print (type(new_qty))
    print('####################')