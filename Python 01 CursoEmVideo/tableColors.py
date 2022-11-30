# ANSI color standard.
# These are the style and color codes that work best in Python.
# Syntax: ``\033[STYLE;FG;BGm``.
# The text must be inserted after the letter ``m``.

# Style:
# - **0**: (Name) without color.
# - **1**: (old) Bold.
# - **4**: (Underline) Underline.
# - **7**: (Negative) Inverts letter and background.

# # Text color (fg):
# - **30**: White.
# - **31**: Red.
# - **32**: Green.
# - **33**: Yellow.
# - **34**: Blue.
# - **35**: Magenta.
# - **36**: Cyan (light blue).
# - **37**: Gray.

# # Background color (bg):
# - **40**: White.
# - **41**: Red.
# - **42**: Green.
# - **43**: Yellow.
# - **44**: Blue.
# - **45**: Magenta.
# - **46**: Cyan (light blue).
# - **47**: Gray.

#     **NOTE**: To clear/limit formatting, use ``\033[m``

style = {'none': 0, 'bold': 1, 'underline': 4, 'invert': 7}

fg = { 'white': 30, 'red': 31, 'green': 32, 'yellow': 33,
      'blue': 34, 'magenta': 35, 'cyan': 36, 'gray': 37}

bg = { 'white': 40, 'red': 41, 'green': 42, 'yellow': 43,
      'blue': 44, 'magenta': 45, 'cyan': 46, 'gray': 47}

if __name__ == '__main__':
    print('Style')
    print(f"\033[{style['none']}m Normal text.")
    print(f"\033[{style['bold']}m Bold text.")
    print(f"\033[{style['underline']}m Underlined text.")
    print(f"\033[{style['invert']}m Text with fg and bg reversed.\n\033[m")

    print('Font Color')
    print('\033[0;30;0m White.')
    print('\033[0;31;0m Red.')
    print('\033[0;32;0m Green.')
    print('\033[0;33;0m Yellow.')
    print('\033[0;34;0m Blue.')
    print('\033[0;35;0m Magenta.')
    print('\033[0;36;0m Cyan.')
    print('\033[0;37;0m Grey.\n\033[m')

    print('Background Color')
    print('\033[0;40;0m White.')
    print('\033[0;41;0m Red.')
    print('\033[0;42;0m Green.')
    print('\033[0;43;0m Yellow.')
    print('\033[0;44;0m Blue.')
    print('\033[0;45;0m Magenta.')
    print('\033[0;46;0m Cyan.')
    print('\033[0;47;0m Grey.\n\033[m')