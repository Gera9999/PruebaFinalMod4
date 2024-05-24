from error import SubTipoInvalidoError

class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        """
        Inicializa una instancia de Anuncio.

        Args:
            ancho (int): Ancho del anuncio.
            alto (int): Alto del anuncio.
            url_archivo (str): URL del archivo del anuncio.
            url_clic (str): URL de clic del anuncio.
            sub_tipo (str): Subtipo del anuncio.
        """
        self.ancho = ancho
        self.alto = alto
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    @property
    def ancho(self):
        """Devuelve el ancho del anuncio."""
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        """Establece el ancho del anuncio, asignando 1 si el valor es menor o igual a cero."""
        self._ancho = value if value > 0 else 1

    @property
    def alto(self):
        """Devuelve el alto del anuncio."""
        return self._alto

    @alto.setter
    def alto(self, value):
        """Establece el alto del anuncio, asignando 1 si el valor es menor o igual a cero."""
        self._alto = value if value > 0 else 1

    @property
    def url_archivo(self):
        """Devuelve la URL del archivo del anuncio."""
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        """Establece la URL del archivo del anuncio."""
        self._url_archivo = value

    @property
    def url_clic(self):
        """Devuelve la URL de clic del anuncio."""
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        """Establece la URL de clic del anuncio."""
        self._url_clic = value

    @property
    def sub_tipo(self):
        """Devuelve el subtipo del anuncio."""
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        """
        Establece el subtipo del anuncio.

        Args:
            value (str): Nuevo subtipo del anuncio.

        Raises:
            SubTipoInvalidoError: Si el subtipo no es válido.
        """
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo inválido: {value}")
        self._sub_tipo = value

    @staticmethod
    def mostrar_formatos():
        """Muestra en pantalla los formatos y sus subtipos disponibles."""
        formatos = [
            (Video.FORMATO, Video.SUB_TIPOS),
            (Display.FORMATO, Display.SUB_TIPOS),
            (Social.FORMATO, Social.SUB_TIPOS)
        ]
        for formato, subtipos in formatos:
            print(f"FORMATO {formato}:\n==========")
            for subtipo in subtipos:
                print(f"- {subtipo}")

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, **kwargs):
        """
        Inicializa una instancia de Video.

        Args:
            kwargs: Argumentos adicionales para la inicialización.
        """
        super().__init__(ancho=1, alto=1, **kwargs)
        self.duracion = kwargs.get('duracion', 5)

    @property
    def duracion(self):
        """Devuelve la duración del video."""
        return self._duracion

    @duracion.setter
    def duracion(self, value):
        """Establece la duración del video, asignando 5 si el valor es menor o igual a cero."""
        self._duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión de video no está implementada."""
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el recorte de video no está implementado."""
        print("RECORTE DE VIDEO NO IMPLEMENTADA AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión de anuncios display no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento de anuncios display no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión de anuncios de redes sociales no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento de anuncios de redes sociales no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
