import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',#pasamos parámetro %s pero dentro del parámetro indicamos que agregue el tiempo, el nivel del mensaje (warning...), el name del archivo que devuelve este mensaje, la línea de código que devuelve este error, y por último el mensaje que hemos agregado.
                datefmt='%I:%M:%S %p',#devuelve horas minutos y segundos y si es am o pm.
                handlers=[
                    log.FileHandler('capa_datos.txt'), #Agrega la info a este archivo
                    log.StreamHandler() #Agrega la info a consola.
                ])



if __name__=='__main__': #Aquí vemos print's de lo que veríamos
    log.debug('Mensaje a nivel debug:')
    log.info('Mensaje a nivel de info:')
    log.warning('Mensaje a nivel de warning:')
    log.error('Mensaje a nivel de error: ')
    log.critical('Mensaje a nivel crítico: ')