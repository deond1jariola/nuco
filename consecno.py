def example_function(*args, **kwargs):
    if args or kwargs:
        print(f"Позиционные аргументы: {args}, Именованные аргументы: {kwargs}")
    else:
        print("Аргументы не переданы.")

example_function()  # Output: "Аргументы не переданы."
example_function('test', key='value')  # Output: "Позиционные аргументы: ('test',), Именованные аргументы: {'key': 'value'}"
