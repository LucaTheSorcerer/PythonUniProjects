class Fractie:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def extinere(self, k):
        self.n *= k
        self.m *= k

    def extinere_new(self, k):
        return Fractie(self.n * k, self.m * k)

    def simplificare(self, k):
        self.n /= k
        self.m /= k

    def print(self):
        print(str(self.n) + '/' + str(self.m))

    def print_fancy(self):
        print(f'{self.n}/{self.m}')

def main():
    f = Fractie(1, 2)

    f.extinere(10)
    f.simplificare(2)
    f.print_fancy()

    g = f.extinere_new(10)
    g.print_fancy()
    f.print_fancy()
main()