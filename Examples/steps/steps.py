from behave import when,given,then
# import user
# import assertions

@given("I create a new User")
def create_new_user(context):
    """_summary_

    Args:
        context (_type_): _description_
    """
    print("I am creating a new user")

@when("I type email")
def type_the_mail(context):
    print("You have typed email")
