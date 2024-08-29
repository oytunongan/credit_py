# TODO
from cs50 import get_string


while True:
    try:
        text = get_string("Number: ")
        count = 0
        x = 0
        for i in range(2, len(text) + 1, 2):
            x = 2 * int(text[0 - i])
            if x > 9:
                count += round(int(x / 10)) + (x % 10)
            else:
                count += x
        for j in range(1, len(text) + 1, 2):
            count += int(text[0 - j])

        if (count % 10) == 0:
            if len(text) == 15 and (int(text[0:2]) == 34 or int(text[0:2]) == 37):
                print("AMEX")
            elif len(text) == 16 and (
                int(text[0:2]) == 51
                or int(text[0:2]) == 52
                or int(text[0:2]) == 53
                or int(text[0:2]) == 54
                or int(text[0:2]) == 55
            ):
                print("MASTERCARD")
            elif (len(text) == 13 or len(text) == 16) and int(text[0:1]) == 4:
                print("VISA")
            else:
                print("INVALID")
        else:
            print("INVALID")
            break
    except ValueError:
        continue
    else:
        break
