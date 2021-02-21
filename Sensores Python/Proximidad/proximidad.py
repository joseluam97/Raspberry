import RPi.GPIO as GPIO
import time

# Pin GPIO donde esta conectado el activador (entrada) del
# sensor HC-SR04.
TRIG = 23

# Pin GPIO donde esta conectado el eco (salida) del sensor
# HC-SR04.
ECHO = 24

# Indicar que se usa el esquema de numeracion de pines
# de BCM (Broadcom SOC channel), es decir los numeros de
# pines GPIO (General-Purpose Input/Output).
GPIO.setmode(GPIO.BCM)

# Establecer que TRIG es un canal de salida.
GPIO.setup(TRIG, GPIO.OUT)

# Establecer que ECHO es un canal de entrada.
GPIO.setup(ECHO, GPIO.IN)

print "Medicion de distancias en progreso"

try:
    # Ciclo infinito.
    # Para terminar el programa se debe presionar Ctrl-C.
    while True:

        # Apagar el pin activador y permitir un par de
        # segundos para que se estabilice.
        GPIO.output(TRIG, GPIO.LOW)
        print "Esperando a que el sensor se estabilice"
        time.sleep(2)

        # Prender el pin activador por 10 microsegundos
        # y despues volverlo a apagar.
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        # En este momento el sensor envia 8 pulsos
        # ultrasonicos de 40kHz y coloca su salida ECHO
        # en HIGH. Se debe detectar este evento e iniciar
        # la medicion del tiempo.
        print "Iniciando eco"
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                break

        # La salida ECHO se mantendra en HIGH hasta recibir
        # el eco reflejado por el obstaculo. En ese momento
        # el sensor pondra ECHO en LOW y se debe terminar
        # la medicion del tiempo.
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                break

        # La medicion del tiempo es en segundos.
        duracion = pulso_fin - pulso_inicio

        # Calcular la distancia usando la velocidad del
        # sonido y considerando que la duracion incluye
        # la ida y vuelta.
        distancia = (34300 * duracion) / 2

        # Imprimir resultado.
        print "Distancia: %.2f cm" % distancia

finally:
    # Reiniciar todos los canales de GPIO.
    GPIO.cleanup()






























