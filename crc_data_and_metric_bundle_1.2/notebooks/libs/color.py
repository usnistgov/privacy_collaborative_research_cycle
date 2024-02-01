import random

# first 11 colors returned by get_colors function.
custom_colors = ["#d62828", "#67f230", "#f77f00", "#0fa3b1", "#548c2f",
                 "#0353a4", "#b532ed", "#b5a264", "#800e13", "#69585f",
                 "#5e503f"]


def get_colors(n: int):
    """
    Get n random colors. First 11 are from list custom_colors.
    n: int - number of colors to return
    returns:
        colors: List[str] - list of colors
    """
    if n < len(custom_colors):
        return custom_colors[:n]
    gen_n = n - len(custom_colors)
    colors = ["#" + ''.join([random.choice('0123456789ABCDEF')
                             for j in range(6)])
              for i in range(gen_n)]
    return custom_colors + colors

