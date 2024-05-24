import sys
from campaña import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError

def main():
    # Información inicial para crear una campaña con un anuncio de tipo Video
    anuncios_info = [
        {"tipo": "Video", "url_archivo": "video.mp4", "url_clic": "http://example.com", "sub_tipo": "instream", "duracion": 10}
    ]

    # Crear una instancia de Campaña
    campaña = Campaña("Campaña Inicial", "2024-01-01", "2024-12-31", anuncios_info)

    # Intentar cambiar el nombre de la campaña
    try:
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        campaña.nombre = nuevo_nombre
    except LargoExcedidoError as e:
        with open("error.log", "a") as error_file:
            error_file.write(f"{e}\n")
        print(e)

    # Intentar cambiar el subtipo del primer anuncio en la campaña
    try:
        nuevo_sub_tipo = input("Ingrese el nuevo sub_tipo para el anuncio: ")
        campaña.anuncios[0].sub_tipo = nuevo_sub_tipo
    except SubTipoInvalidoError as e:
        with open("error.log", "a") as error_file:
            error_file.write(f"{e}\n")
        print(e)

if __name__ == "__main__":
    main()
