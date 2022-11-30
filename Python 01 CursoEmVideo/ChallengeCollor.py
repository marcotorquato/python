
class ANSI():
	def background(code):
		return "\33[{code}m".format(code=code)

	def style_text(code):
		return "\33[{code}m".format(code=code)

	def color_text(code):
		return "\33[{code}m".format(code=code)


example_ansi = ANSI.background(
	97) + ANSI.color_text(35) + ANSI.style_text(4) + " TESTE ANSI ESCAPE CODE"
print(example_ansi)

# style 0, 1, 4 e 7,
# text 30 - 37,
# background 40 - 47,
# \033[0;33;44m,
# or installing the library termcolor exemple: 

from termcolor import colored

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])

print(text)
