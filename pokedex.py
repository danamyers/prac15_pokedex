import requests

def obtener_pokemon():
    nombre = input("🔎 Ingresa el nombre del Pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza un error si la solicitud falla
        
        datos = respuesta.json()
        nombre_pokemon = datos["name"].capitalize()  # Corregido: 'dotos' -> 'datos'
        altura = datos["height"] / 10  # Convertir a metros
        peso = datos["weight"] / 10  # Convertir a kg
        numero_pokedex = datos["id"]  # Corregido: 'numeros_pokedex' -> 'numero_pokedex'
        
        tipos = [tipo["type"]["name"].capitalize() for tipo in datos["types"]]
        habilidades = [hab["ability"]["name"].capitalize() for hab in datos["abilities"]]

        print("\n📖 POKEDEX")
        print(f"🔢 Número: {numero_pokedex}")
        print(f"🐉 Nombre: {nombre_pokemon}")
        print(f"📏 Altura: {altura} metros")  # Corregido: 'mnetros' -> 'metros'
        print(f"⚖ Peso: {peso} kg")
        print(f"🔥 Tipo(s): {', '.join(tipos)}")  # Corregido: 'Tipo(s:' -> 'Tipo(s):'
        print(f"💡 Habilidades: {', '.join(habilidades)}")
    
    except requests.exceptions.HTTPError:  # Corregido: 'exceptiones' -> 'exceptions'
        print("❌ Pokémon no encontrado. Intenta nuevamente.")
    except requests.exceptions.RequestException:
        print("❌ Error de conexión con la API.")  
    except Exception as e: 
        print(f"❌ Error inesperado: {e}")  # Corregido: 'imesoerado' -> 'inesperado'

# Llamar a la función para que el usuario ingrese un Pokémon
obtener_pokemon()