from pygments.token import Whitespace, Token, Comment, String

class TokenCounter:
    def __init__(self) -> None:
        pass

    @staticmethod
    def count_tokens(lexer, text):
        count = 0 
        for token in lexer.get_tokens_unprocessed(text):
            _, token_type, token_val = token
            if not ( token_type is Whitespace or token_type is Token.Text.Whitespace or token_val.isspace() or token_val  == ''):
                count += 1
        return count