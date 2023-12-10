class MyCustomError(TypeError):
    """
    this error is thrown when a certain error code is needed to process the exception
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    
    def __init__(self, mesage, code) -> None:
        super().__init__(f'Error code {code}: {mesage}')
        self.code = code



err = MyCustomError('I have experienced an error', 400)
print(err.__doc__)

