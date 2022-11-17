from behave import when,given,then
# import user
# import assertions

@given("I create a new User")
def create_new_user(context):
    """_summary_

    Args:
        context (_type_): _description_
    """
    with open("sample.txt",'w') as fp:
        fp.write("Hello")
    print("I am creating a new user")

@when("I type email")
def type_the_mail(context):
    print("You have typed email")

@when('I execute using handler {Node2} the SSH command {command}')
def ssh(context,Node1,command):
    with open("../config/config.properties") as fp:
        data = fp.readlines()

    

