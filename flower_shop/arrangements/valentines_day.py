from .arrangement import Arrangement
from flowers import IValentines

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        if isinstance(flower, IValentines):
            self.flowers.append(flower)
        else:
            print(f'{flower} does not belong in the Valentines Day arrangement. Please choose a Rose, Lily, or Alstroemeria ')

    