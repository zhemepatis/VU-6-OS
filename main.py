# from real_machine import RealMachine
from resources.resource import *
from resources.create_file import *

# real_machine = RealMachine()
# real_machine.run()

rsc = Resource("aa")
print(rsc.name)

rsc = CreateFile("bb")
print(rsc.name)

