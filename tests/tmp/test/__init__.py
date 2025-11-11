from pyre import executive

package = executive.registerPackage(name="test", file=__file__)
home, prefix, defaults = package.layout()
