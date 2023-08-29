# importaciones
import os

from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

pokemones = [{'Nombre': "Pikachu","Tipo":"Fuego","Poder":100}]

anime = [
    {"ID": 1, "nombre": "Anime A", "categoria": "Aventura", "rating": 4.5, "reviews": 120, "season": "Verano", "tipo": "TV","poster":"img1.png"},
    {"ID": 2, "nombre": "Anime B", "categoria": "Comedia", "rating": 3.8, "reviews": 80, "season": "Otoño", "tipo": "TV","poster":"img1.png"},
    {"ID": 3, "nombre": "Anime C", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno", "tipo": "Película","poster":"img1.png"},
    {"ID": 4, "nombre": "Anime D", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"},
    {"ID": 5, "nombre": "Anime E", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"},
    {"ID": 6, "nombre": "Anime F", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"},
    {"ID": 7, "nombre": "Anime F", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"},
    {"ID": 8, "nombre": "Anime F", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"},
    {"ID": 9, "nombre": "Anime F", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"},
    {"ID": 10, "nombre": "Anime F", "categoria": "Drama", "rating": 4.0, "reviews": 150, "season": "Invierno",
     "tipo": "Película", "poster": "img1.png"}
]
@app.route('/')
def inicio():
    return "hola anime"

@app.route('/anime', methods=['GET'])
def mostrar_anime():
    return jsonify(anime)
@app.route('/anime', methods=['POST'])
def agregar_anime():
    nuevo_anime = request.get_json()
    print("hola")

    # Asigna un ID único al nuevo anime
    nuevo_anime_id = max([anime_item["ID"] for anime_item in anime]) + 1
    nuevo_anime["ID"] = nuevo_anime_id
    anime.append(nuevo_anime)
    return jsonify({"mensaje": "Nuevo anime agregado exitosamente"})

@app.route('/anime/<int:anime_id>', methods=['GET'])
def obtener_anime(anime_id):
    for anime_item in anime:
        if anime_item["ID"] == anime_id:
            return jsonify(anime_item)

    return jsonify({"mensaje": "Anime no encontrado"}), 404

@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def eliminar_anime(anime_id):
    global anime

    anime_temp = anime.copy()  # Copia temporal para evitar problemas de iteración y modificación
    for anime_item in anime_temp:
        if anime_item["ID"] == anime_id:
            anime.remove(anime_item)
            return jsonify({"mensaje": f"Anime con ID {anime_id} eliminado correctamente"})

    return jsonify({"mensaje": "Anime no encontrado"}), 404


@app.route('/anime/<int:anime_id>', methods=['PUT'])
def modificar_anime(anime_id):
    global anime

    anime_data = request.get_json()

    for anime_item in anime:
        if anime_item["ID"] == anime_id:
            anime_item.clear()
            anime_item.update(anime_data)
            anime_item["ID"] = anime_id # ID NO PUEDE CAMBIARSE
            return jsonify({"mensaje": f"Anime con ID {anime_id} modificado correctamente"})

    return jsonify({"mensaje": "Anime no encontrado"}), 404

@app.route('/anime/<int:anime_id>', methods=['PATCH'])
def modificar_parcial_anime(anime_id):
    global anime

    anime_data = request.get_json()

    for anime_item in anime:
        if anime_item["ID"] == anime_id:
            anime_item.update(anime_data)
            keys_to_remove = []     #lista de key a remover
            for key, value in anime_data.items():
                if value == "":
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                anime_item.pop(key)
            anime_item["ID"] = anime_id # ID NO PUEDE CAMBIARSE
            return jsonify({"mensaje": f"Anime con ID {anime_id} modificado parcialmente correctamente"})

    return jsonify({"mensaje": "Anime no encontrado"}), 404



if __name__ == '__main__':
    app.run(debug=True)
else:
    print('Importing {}'.format(__name__))
