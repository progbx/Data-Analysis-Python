__Task description__

Consider functions that accept keyword arguments only and develop a decorator called debug applicable to them that prints the name of a function and, optionally, the names of its arguments and their respective values before calling the function. The decorator should have the boolean argument __print_arguments__ with the default value True, which controls whether to print a function's arguments or not. The message printed by the decorator should be in the following format:

__Calling a function "<function_name>" [with the arguments <arg_1>=<value_1>, <arg_2>=<value_2>[, ...]__

_Note 1_. The decorator will be tested against functions with integer-valued arguments only.

_Note 2_. You can use the __name__ attribute of a function to get its name.

<br>

__Test data sets examples__

| № | Input data | Expected output |
|----------|----------|----------|
| 1    | def identity(x=0): return x / print_arguments=False   | Calling a function "identity"  |
| 2    | def compute(a=1, b=2, c=3): return (a + b) * c / print_arguments=True | Calling a function "compute" with the arguments a=1, b=2, c=3  |