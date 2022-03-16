import webbrowser

print(100 * '*')

# **************************************************************************
uno = 1
dos = 2 
op = input('Abrir ventana (1)\nAbrir pestaña (2)\nRespuesta:')
while op:
    if op == 1:
        print(page)
        break
    elif op == 2:
        print(page_)
        break    
    else:
        try: 
            op == str(input)
        except ValueError:
            print(op)
        break
#Primero específicamos el buscador que usaremos
browser = webbrowser.register('chrome', None, False)

# Abrir una ventana

page = input('Ingrese la página que desea abrir:')
open_w = webbrowser.open_new(url="{0}".format(page))

# Abrir nueva pestaña

page_ = (input('Ingrese la pestaña que desea abrir'))
open_other_w = webbrowser.open_new_tab(url="{0}".format(page_))



# ***************************************************************************







