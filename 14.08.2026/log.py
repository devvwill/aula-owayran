from venve import log

def loq_execucao (func): 
    @functtools.wraps (func) 
    def wrapper (*args, **kwargs):
        logger.info ("inicio: %s", func._name_)
        resultado = func(*args, **kwargs)
        logger.info ("fim: %s", func._name_)
        return resultado
    return wrapper