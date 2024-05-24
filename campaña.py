from datetime import date
from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoError

class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_info):
        """
        Inicializa una instancia de Campaña.

        Args:
            nombre (str): Nombre de la campaña.
            fecha_inicio (date): Fecha de inicio de la campaña.
            fecha_termino (date): Fecha de término de la campaña.
            anuncios_info (list): Lista de diccionarios con la información de los anuncios.
        """
        self._nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_info)

    def _crear_anuncios(self, anuncios_info):
        """
        Crea anuncios a partir de la información proporcionada.

        Args:
            anuncios_info (list): Lista de diccionarios con la información de los anuncios.

        Returns:
            list: Lista de instancias de anuncios.
        """
        anuncios = []
        for info in anuncios_info:
            tipo = info['tipo']
            if tipo == 'Video':
                anuncios.append(Video(**info))
            elif tipo == 'Display':
                anuncios.append(Display(**info))
            elif tipo == 'Social':
                anuncios.append(Social(**info))
        return anuncios

    @property
    def nombre(self):
        """Devuelve el nombre de la campaña."""
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        """
        Establece el nombre de la campaña.

        Args:
            value (str): Nuevo nombre de la campaña.

        Raises:
            LargoExcedidoError: Si el nombre excede los 250 caracteres.
        """
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña no puede exceder los 250 caracteres.")
        self._nombre = value

    @property
    def anuncios(self):
        """Devuelve la lista de anuncios de la campaña."""
        return self._anuncios

    def __str__(self):
        """Devuelve una representación en cadena de la campaña."""
        count = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self._anuncios:
            count[type(anuncio).FORMATO] += 1

        return (f"Nombre de la campaña: {self._nombre}\n"
                f"Anuncios: {count['Video']} Video, {count['Display']} Display, {count['Social']} Social")
