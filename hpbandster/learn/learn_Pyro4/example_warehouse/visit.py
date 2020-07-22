# This is the code that visits the warehouse.
import sys
import Pyro4
import Pyro4.util
from person import Person

sys.excepthook = Pyro4.util.excepthook

# uri = input("Enter the uri of the warehouse: ").strip()
warehouse = Pyro4.Proxy("PYRONAME:example.warehouse")
janet = Person("Janet")
henry = Person("Henry")
janet.visit(warehouse)
henry.visit(warehouse)