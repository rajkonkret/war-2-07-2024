def all_args(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)


all_args()
all_args(1, 2, 3, 4, 5, 6)
all_args(a=1, b=2, c=3, d=4, e=5, f=6)
all_args(1, 2, c=3, d=4, e=5, f=6)
# args ()
# kwargs {}
# args (1, 2, 3, 4, 5, 6)
# kwargs {}
# args ()
# kwargs {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# args (1, 2)
# kwargs {'c': 3, 'd': 4, 'e': 5, 'f': 6}
# argumenty pozycyjne nie mogą być po nazwanych !!!
# all_args(a=6, 2)  # SyntaxError: positional argument follows keyword argument
