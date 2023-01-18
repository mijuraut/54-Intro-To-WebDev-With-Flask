import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("Greetings")

say_greeting()

# decorated_function = delay_decorator(say_greeting)
# decorated_function()