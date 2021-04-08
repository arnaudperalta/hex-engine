from IPython.display import SVG, display

def display_cell(position: int, color):
	display(SVG(url='https://upload.wikimedia.org/wikipedia/commons/a/a0/Circle_-_black_simple.svg'))

def display_board():
	display(SVG(url='https://upload.wikimedia.org/wikipedia/commons/e/e9/Hex_board_11x11.svg'))
