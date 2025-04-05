# CONSTANTE = Variáveis que não mudam (Escritas em letra Maiúscula)
# "\" -> Quebra de linha no código

velocidade = 61
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_car_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_car_pass_radar_1

if vel_car_pass_radar_1:
    print("O carro ultrapassou a velocidade limite do radar 1")

if carro_passou_radar_1:
    print("O carro passou em radar 1")

if carro_multado_radar_1:
    print("O carro multado em radar 1")