class Foo:
    field = "foo"
    

class Baz:
    field = "baz"
    

class Bar(Baz, Foo):
    pass


bar = Bar()

print(bar.field)
