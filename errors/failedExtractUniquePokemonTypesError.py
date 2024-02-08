class FailedExtractUniquePokemonTypesError(Exception):
    """Custom exception for failed extraction of unique Pokemon types."""

    def __init__(self, original_exception=None):
        self.message = "Failed to extract unique Pokemon types."
        self.original_exception = original_exception
        super().__init__(self.message)

    def __str__(self):
        if self.original_exception:
            return f"{self.message} Original Exception: {self.original_exception}"
        return self.message
