from arrangements import MothersDay, ValentinesDay
from flowers import Rose, Daisy, Lily, Alstroemeria

if __name__ == "__main__":
    for_beth = ValentinesDay()
    red_rose = Rose()
    ugly_daisy = Daisy()

    for_beth.enhance(red_rose)
    for_beth.enhance(ugly_daisy)