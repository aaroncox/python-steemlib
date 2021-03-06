class Amount(object):
    def __init__(self, amountString="0 SBD"):
        self.amount, self.asset = amountString.split(" ")
        if self.amount:
            self.amount = float(self.amount)
        else:
            self.amount = 0.0

    def __str__(self):
        if self.asset == "SBD":
            prec = 3
        elif self.asset == "STEEM":
            prec = 3
        elif self.asset == "VESTS":
            prec = 6
        else:
            prec = 6
        return "{:.{prec}f} {}".format(self.amount, self.asset, prec=prec)

    def __float__(self):
        return self.amount

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        a = Amount(str(self))
        if isinstance(other, Amount):
            assert other.asset == self.asset
            a.amount += other.amount
        else:
            a.amount += float(other)
        return a

    def __sub__(self, other):
        a = Amount(str(self))
        if isinstance(other, Amount):
            assert other.asset == self.asset
            a.amount -= other.amount
        else:
            a.amount -= float(other)
        return a

    def __mul__(self, other):
        a = Amount(str(self))
        a.amount *= other
        return a

    def __floordiv__(self, other):
        a = Amount(str(self))
        a.amount //= other
        return a

    def __div__(self, other):
        a = Amount(str(self))
        a.amount /= other
        return a

    def __mod__(self, other):
        a = Amount(str(self))
        a.amount %= other
        return a

    def __pow__(self, other):
        a = Amount(str(self))
        a.amount **= other
        return a

    def __iadd__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            self.amount += other.amount
        else:
            self.amount += other
        return self

    def __isub__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            self.amount -= other.amount
        else:
            self.amount -= other
        return self

    def __imul__(self, other):
        self.amount *= other
        return self

    def __idiv__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount / other.amount
        else:
            self.amount /= other
            return self

    def __ifloordiv__(self, other):
        self.amount //= other
        return self

    def __imod__(self, other):
        self.amount %= other
        return self

    def __ipow__(self, other):
        self.amount **= other
        return self

    def __lt__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount < other.amount
        else:
            return self.amount < float(other or 0)

    def __le__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount <= other.amount
        else:
            return self.amount <= float(other or 0)

    def __eq__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount == other.amount
        else:
            return self.amount == float(other or 0)

    def __ne__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount != other.amount
        else:
            return self.amount != float(other or 0)

    def __ge__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount >= other.amount
        else:
            return self.amount >= float(other or 0)

    def __gt__(self, other):
        if isinstance(other, Amount):
            assert other.asset == self.asset
            return self.amount > other.amount
        else:
            return self.amount > float(other or 0)

    __repr__ = __str__


if __name__ == "__main__":
    a = Amount("2 SBD")
    b = Amount("9 SBD")
    print(a + b)
    print(b)
    b **= 2
    b += .5
    print(b)
    print(b > a)

    c = Amount("100 STEEM")
    print(c * .10)

    # print(a + c)
    # print(a < c)
