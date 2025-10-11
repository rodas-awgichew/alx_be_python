class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """Performs addition without accessing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Performs multiplication and references a class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b