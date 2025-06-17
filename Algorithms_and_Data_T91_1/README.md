__Task description__

Implement a function that executes any function with an arbitrary number of arguments and tracks whether an exception occurred as follows:

If the input function raises an exception, the current function must print a message in the format ```<ExceptionType>: <ExceptionMessage>```.

If the input function does not raise an exception, the current function must print the message ```No exception raised```

After execution of the input function is ended, the current function must print the message ```Execution of the function <InputFunctionName> is ended```.

<br>

__Test data sets examples__

| № | Input data | Expected output |
|----------|----------|----------|
| 1    | def raise_value_error(): raise ValueError("Error") / [ ] / dict()   | ValueError: Error.Execution of the function raise_value_error ended.  |
| 2    | def power(x, n=2): return x ** n / [2] / dict(n=3) | No exception raised.Execution of the function power ended.  |