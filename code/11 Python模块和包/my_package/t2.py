
import my_package
print([e for e in dir(my_package) if not e.startswith('_')])
# help(my_package.module1)