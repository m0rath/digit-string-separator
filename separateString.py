
# This program helps to separate string with integer

class separateString:

    def __init__(self, data):
        self.data = data

    def bifurcate(self):
        try:
            digits, other_ltr = "", ""
            for ltr in self.data:
                if ltr.isdigit():
                    digits = digits + ltr
                else:
                    other_ltr = other_ltr + ltr
            return int(digits), other_ltr
        except Exception as e:
            print("Error msg: ", e)


if __name__ == '__main__':
    try:
        strings = separateString("test123er34")
        print(strings.bifurcate())
    except TypeError as te:
        print("Argument assignment failed: ", te)
    except Exception as e:
        print("Error msg: ", e)
