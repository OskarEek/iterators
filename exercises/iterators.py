"""Övningar på iterators."""


class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number ** 3




class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    pass
    def __init__(self):
        self.number = 1
        self.primes = []
        self.y = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.number % self.y == 0:
            Primes.is_prime(i)
        #while self.y < self.number and self.y > 1:
        #   self.y += 1


        #    x = self.number / self.y
        #    if isinstance(x, int) == false:
        #        self.primes.append(self.number)
        #        return primes
        #    else:
        #        self.number += 1

#    @staticmethod
#    def is_prime(x):


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        self.numbers = [0, 1]
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count < 1:  # First two numbers.
            self.count += 1
            return self.count

        n = self.numbers[0] + self.numbers[1]  # nästa värde
        self.numbers[0] = self.numbers[1]
        self.numbers[1] = n
        return n



class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    def __init__(self):
        self.a = 0
        self.b = 1
        self.names = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
                        'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem',
                        'Nun', 'Samekh', 'Ayin', 'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.names) <= self.a:
            raise StopIteration

        b = self.names[self.a]
        self.a += 1
        return b


class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    pass


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    pass
