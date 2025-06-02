### title

00-do-abstract-parents-pass-their-variables-onto-their-children
This is a title.

# About

This is a miniproject from a doubt I had, literally, in my sleep.
I dreamed of accessing some variable stored within an abstract base class.
The following hypothesis was formulated:
```
Let A be an abstract base class with a method m() and a variable _v.

'Abstract parents pass their variables onto their concrete children'(from title) in case a child B, who inherits A, is implemented doing overlapping only on the method m(), not the variable _v. 
The title would be true if and only if B._v is called successfully, not throwing any errors.
```

# How

Three files were created in Vim importing ```abc``` to the first one. `children\.py` reads from `parents.*\.py` matching files.

# Conclusion 

```
# Output: vee

Finally we made it, the variable was acquired without throwing anything.
This means:... 
**NO**, abstract parents do not pass their variables on. Though this does not mean abstract classes withhold their variables from their children - a child just needs to reach out and ask.
It can be done through localized access (imprecise name) in the form of:...

'self._v = A._v'
```
