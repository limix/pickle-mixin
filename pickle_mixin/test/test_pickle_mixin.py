import pickle
from pickle import PicklingError

import pytest

from pickle_mixin import SlotPickleMixin

class Foo(object):
    __slots__ = ['a']
    def __init__(self):
        self.a = 4

class Bar(Foo):
    def __init__(self):
        pass

class FooMixin(object):
    __slots__ = ['a']
    def __init__(self):
        self.a = 4

class BarMixin(FooMixin, SlotPickleMixin):
    def __init__(self):
        FooMixin.__init__(self)
        SlotPickleMixin.__init__(self)

def test_pickle_mixin():
    f = Bar()
    o = pickle.dumps(f)
    f = pickle.loads(o)
    assert not hasattr(f, 'a')
    f = BarMixin()
    o = pickle.dumps(f)
    f = pickle.loads(o)
    assert hasattr(f, 'a')
