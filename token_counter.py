class TokenCounter:
    def __init__(self) -> None:
        pass

    @staticmethod
    def count_tokens(lexer, text):
        return sum(1 for _ in lexer.get_tokens_unprocessed(text))