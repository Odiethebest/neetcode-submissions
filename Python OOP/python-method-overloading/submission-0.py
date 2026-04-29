class TextProcessor:
    # Implement method overloading for format_text method
    def __init__(self):
        pass

    def format_text(self, arg1: str, arg2: str = None) -> str:
        if arg2 is None:
            return arg1.upper()
        else:
            return arg1 + arg2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
