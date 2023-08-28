from settings import *

# States
class Form(StatesGroup):
    chating = State()  # Will be represented in storage as 'Form:mail'
