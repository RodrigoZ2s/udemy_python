EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time): 
    """ 
    Função que calcula o tempo do bolo

    Recebe "elapsed_bake_time" como parâmetro
    retorna o tempo esperado de cozimento menos o tempo que já passou

    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    return 2 * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    layers = preparation_time_in_minutes(number_of_layers)
    time = bake_time_remaining(elapsed_bake_time)
    return layers + time

