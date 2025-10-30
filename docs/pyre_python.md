# Pyre Python implementation

## Protocol

```python
class Foo(pyre.protocol, family="pylith.foo"):

    @classmethod
    def pyre_default(cls, **kwds):
        """The default implementation"""
        return Bar

    @pyre.provides
    def doit(self, argument):
        """Protocol method"""
```

## Implementation

```python
class FooBar(pyre.component, family="pylith.foo.foobar"):

    from MyComponent import MyComponent

    my_component = MyComponent()
    my_component.doc = "My component documentation"

    value = pyre.properties.dimensional(default=1.0 * meter)
    value.doc = "Property value."

    @pyre.export
    def foobar(self, argument):
        """Define method"""
        my_component = argument
```
