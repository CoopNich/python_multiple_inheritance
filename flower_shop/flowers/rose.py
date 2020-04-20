from flowers import Flower
from .valentines_flower import IValentines

class Rose(Flower, IValentines):

    def __init__(self):
        Flower.__init__(self)
        IValentines.__init__(self)