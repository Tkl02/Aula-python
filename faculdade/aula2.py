#leito de bateria

import psutil  # importa biblioteca psutil(monitoramento de sistema)

bateria = psutil.sensors_battery() # acesso o sensor da bateria
nivel = str(bateria.percent) # capturar o nivel da bateria 
print('bateria {}%'.format(nivel)) # mostrar o nivel da bateria
