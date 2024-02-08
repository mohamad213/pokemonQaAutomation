class UnsupportedPokemonTypeError(Exception):
    """Custom exception for unsupported Pokemon type."""

    def __init__(self, pokemon_type):
        self.message = f"unsupported Pokemon type {pokemon_type}"
        super().__init__(self.message)
