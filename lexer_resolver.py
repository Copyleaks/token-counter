from pygments.lexers.markup import TexLexer
from pygments.lexers.php import PhpLexer
from pygments.lexers.perl import PerlLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.go import GoLexer 
from pygments.lexers.dotnet import CSharpLexer
from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexers.objective import ObjectiveCLexer, SwiftLexer
from pygments.lexers.ruby import RubyLexer
from pygments.lexers.shell import BashLexer
from pygments.lexers.jvm import ScalaLexer, JavaLexer
from pygments.lexers.javascript import JavascriptLexer, TypeScriptLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.rust import RustLexer
from pygments.lexers.basic import VBScriptLexer
from pygments.lexers.matlab import MatlabLexer
from pygments.lexers.css import CssLexer
import os

class LexerResolver:
    @staticmethod
    def get_file_extension(filename):
        _, file_extension = os.path.splitext(filename)
        return file_extension
    
    @staticmethod
    def get_lexer_for_filetype(filename):
        file_extension = LexerResolver.get_file_extension(filename)
        if file_extension in LexerResolver.FILE_TYPE_TO_LEXER:
            return LexerResolver.FILE_TYPE_TO_LEXER[file_extension]
        raise KeyError(f"Failed to get Lexer, unsupported file type {file_extension}")

    @staticmethod
    def is_file_extension_supported(filename):
        return LexerResolver.get_file_extension(filename) in LexerResolver.FILE_TYPE_TO_LEXER

    
    # Lexers 
    TEX_LEXER = TexLexer()
    PYTHON_LEXER = PythonLexer()
    GO_LEXER = GoLexer()
    C_SHARP_LEXER = CSharpLexer()
    C_LEXER = CLexer()
    CPP_LEXER = CppLexer()
    JAVA_LEXER = JavaLexer()
    JAVA_SCRIPT_LEXER = JavascriptLexer()
    SWIFT_LEXER = SwiftLexer()
    RUBY_LEXER = RubyLexer()
    PERL_LEXER = PerlLexer()
    PHP_LEXER = JavascriptLexer()
    BASH_LEXER = BashLexer()
    OBJECTIVE_C_LEXER = ObjectiveCLexer()
    SCALA_LEXER = ScalaLexer()
    TYPE_SCRIPT_LEXER = TypeScriptLexer()
    HTML_LEXER = HtmlLexer()
    RUST_LEXER = RustLexer()
    VB_LEXER = VBScriptLexer()
    MAT_LAB_LEXER = MatlabLexer()
    CSS_LEXER = CssLexer()

    FILE_TYPE_TO_LEXER = {
        '.py' : PYTHON_LEXER,
        '.go' : GO_LEXER,
        '.cs' : C_SHARP_LEXER,
        '.c' : C_LEXER,
        '.cpp' : CPP_LEXER,
        '.java' : JAVA_LEXER,
        '.js' : JAVA_SCRIPT_LEXER,
        '.swift' : SWIFT_LEXER,
        '.rb' : RUBY_LEXER,
        '.pl' : PERL_LEXER,
        '.php' : PHP_LEXER,
        '.sh' : BASH_LEXER,
        '.vbs' : VB_LEXER,
        '.ts' : TYPE_SCRIPT_LEXER,
        '.hh' : OBJECTIVE_C_LEXER,
        '.scala' : SCALA_LEXER,
        '.m' : MAT_LAB_LEXER,
        '.rs' : RUST_LEXER,
        '.css': CSS_LEXER
    }