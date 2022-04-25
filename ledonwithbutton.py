#estructura de codigo de micropython
import time
#permite acceder a los pines de la placa
import machine

#variables
tiempo= 100 #ms
#configuracion de los pines GPIO permiten hacer control pwm, dac, comunicacion
#los parametros que se configuran (pin_a_usar, modo_de_uso) en este caso sera entrada(IN)
boton = machine.Pin(4, machine.Pin.IN) #entrada digital
led = machine.Pin(2, machine.Pin.OUT) # salida digital

#codigo
"""hacer que un led se encienda al presionar un boton si el boton no se presiona el led se apaga"""

while True:

    if (boton.value()):
        led.on()
        print("boton presionado")
        time.sleep_ms(tiempo)



