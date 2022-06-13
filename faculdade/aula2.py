#leito de bateria

import psutil  #biblioteca 

# acesso o sensor da bateria
bateria = psutil.sensors_battery() 
# #capturar o nivel da bateria 
nivel = str(bateria.percent)
# #mostrar o nivel da bateria
print('bateria {}%'.format(nivel))
