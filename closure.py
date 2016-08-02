def print_msg(msg):
    """This is the outer enclosing function"""

    def printer(m):
        """This is the nested function"""
        print(msg+" "+m)

    return printer  # this got changed

a = print_msg("Hello")
a("world")