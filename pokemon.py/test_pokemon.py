from pokemon import calcula_pontos_ataque, pokemon_evoluiu

# Testes para calcula_pontos_ataque
def test_calcula_pontos_ataque_1():
    pokemon = {"forca_base": 10, "nivel": 1}
    assert calcula_pontos_ataque(pokemon) == 10

def test_calcula_pontos_ataque_2():
    pokemon = {"forca_base": 5, "nivel": 0}
    assert calcula_pontos_ataque(pokemon) == 0

def test_calcula_pontos_ataque_3():
    pokemon = {"forca_base": 20, "nivel": 5}
    assert calcula_pontos_ataque(pokemon) == 100

# Testes para pokemon_evoluiu
def test_pokemon_evoluiu_1():
    pokemon = {"nivel": 15}
    assert pokemon_evoluiu(pokemon, 20) is False

def test_pokemon_evoluiu_2():
    pokemon = {"nivel": 20}
    assert pokemon_evoluiu(pokemon, 20) is True

def test_pokemon_evoluiu_3():
    pokemon = {"nivel": 25}
    assert pokemon_evoluiu(pokemon, 20) is True