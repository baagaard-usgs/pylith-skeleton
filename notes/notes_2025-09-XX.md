1. journal output has the form `NAME: message`. The name seems to come from the name of the application. How is it set? Should it be common across a library?
2. If I have an object (class) that reuses the same journal channel in multiple places, is it worth creating a class attribute/member? Where should it be created? A class attribute has the name "journal" the first time it is used, and then the application name for remaining uses.
3. Should I use `self.pyre_name` in the journal message? Is there a better way to include the Pyre name in the journal output?
4. 