from random import randint


class PasswordGenerator:
    length = 0
    password = ""

    def set_length(self, length):
        self.length = length

    def get_password(self):
        return self.password

    #def print(self):
    #    print(self.password)

    def random_number(self):
       rand_num = randint(33, 126) #ASCII table !(33) to ~(126) -- before and after those decimals are null characters
       return rand_num

    def ascii_selector(self):
        char = chr(self.random_number())
        return char

    def make_password(self):
        for _ in range(self.length):
            self.password += str(self.ascii_selector())