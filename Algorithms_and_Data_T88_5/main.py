def debug(print_arguments=True):
    def decorator(f):
        """
        Decorates the function and prints its name and possibly
        its keyword arguments (depending on the value of the
        `print_arguments` parameter)
        """
        def wrapper(*args, **kwargs):
            # Print function name
            message = f'Calling a function "{f.__name__}"'
            
            if print_arguments:
                # If print_arguments is True, print arguments in the required format
                arguments = ', '.join(f'{k}={v}' for k, v in kwargs.items())
                message += f' with the arguments {arguments}'
            
            print(message)
            return f(*args, **kwargs)
        
        return wrapper
    return decorator
