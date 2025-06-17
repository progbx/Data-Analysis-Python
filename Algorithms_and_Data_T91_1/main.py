def track_exceptions(function, *args, **kwargs):
    """
    Calls any function with an arbitrary number of arguments
    and tracks whether an exception occurred.
    """
    try:
        result = function(*args, **kwargs)
        print("No exception raised.")
    except Exception as e:
        print(f"{type(e).__name__}: {e}.")  # Added a period at the end of the exception message
    finally:
        print(f"Execution of the function {function.__name__} ended.")  # Correct format

    return result if 'result' in locals() else None  # Return None if an exception occurs
