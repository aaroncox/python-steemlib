import steem as stm
from .exceptions import WitnessDoesNotExistsException


class Witness(dict):
    def __init__(
        self,
        witness,
        steem_instance=None,
        lazy=False
    ):
        self.cached = False
        self.witness = witness

        if not steem_instance:
            steem_instance = stm.Steem()
        self.steem = steem_instance

        if not lazy:
            self.refresh()

    def refresh(self):
        witness = self.steem.rpc.get_witness_by_account(self.witness)
        if not witness:
            raise WitnessDoesNotExistsException
        super(Witness, self).__init__(witness)
        self.cached = True

    def __getitem__(self, key):
        if not self.cached:
            self.refresh()
        return super(Witness, self).__getitem__(key)

    def items(self):
        if not self.cached:
            self.refresh()
        return super(Witness, self).items()
