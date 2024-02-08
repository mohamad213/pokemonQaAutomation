class FailedGetPokemonTypeUrlError(Exception):
    """Custom exception for failed get pokemon type url."""

    def __init__(self, original_exception=None):
        self.message = "Failed get pokemon type url."
        self.original_exception = original_exception
        super().__init__(self.message)

    def __str__(self):
        if self.original_exception:
            return f"{self.message} Original Exception: {self.original_exception}"
        return self.message
