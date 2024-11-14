# hayashiel
# 10-17-24
# https://peps.python.org/pep-0008/#comments
# https://realpython.com/documenting-python-code/

# This is the first class I am defining according to PEP 8. This makes two lines - a block comment.
# This continues with the second line and the third line here.
# Then there is a paragraph end.

# Thus, class begins.
class HelloWorldSoftware:
    """ Follow PEP 257 here. 
    Return "Hello World"
    """
    def __init__(self):
        print("Hello World")                     # A start of Coding
        # TODO: Add another few files with Software Testing Material
        # BUG: Why are there lightbulbs on this sentence?

# Instantiate the HelloWorldSoftware class.  
if __name__ == "__main__":
    s = HelloWorldSoftware()
