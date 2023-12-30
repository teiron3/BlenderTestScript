import my
import my.def3
import my.def1

# import def3
# import def1
import importlib

importlib.reload(my.def1)
importlib.reload(my.def3)
d = my.def1
d3 = my.def3
x = 4
d.all_clear()
d3.testmeth001()
# d.testfn12()
