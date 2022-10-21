import random
import string
class RandomDataclass:
    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))  # generate random data

