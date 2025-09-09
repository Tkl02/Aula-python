a_point = (10,20)
print(f"ponto a {a_point}")

red_color = (255,0,0)
x_coordinates = a_point[0]
print(f"Coordenadas ponta a: {x_coordinates}")

try:
    a_point[0] = 15
except TypeError as error:
    print(f"erro ao tentar mudar indice {error}")


map_locations = {}

map_locations [(10,20)] = "Brazil"
map_locations [(30,40)] = "China"
map_locations [(50,60)] = "Japão"

print(f"local no mapa: {map_locations}")
print(f"local selecionado {map_locations[(50,60)]}")
