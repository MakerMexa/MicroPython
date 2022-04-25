#modulos o librerias con micropython
#es un codigo que debido a que cumple con los principios de la progracion es aplicable en la mayoria de casos

import time as tm
import machine as mch

def blink(duracion, cant, npin):
    """esta funcion hace parpadear un led .
    nPin: indica el pin el que esta conectado el led.
    duracion: controla el tiempo en el cual el led prende y apaga.
    cant: indica la cantidad maxima de veces que el led parpadea"""

    led = mch.Pin(npin, mch.Pin.OUT)

    #ciclo for para control on/off del led

    for x in range(cant):
        led.on()
        tm.sleep_ms(duracion)
        led.off()
        tm.sleep_ms(duracion)

    return('DONE!')



