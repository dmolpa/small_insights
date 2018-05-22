from library import Base

#check if methods are available from library
assert hasattr(Base, 'foo'), 'You broke foo in the library!'

class Derived(Base):
    def bar(self):
        return self.foo()