Script en python para extraer la informacion del tamaño de los streams de un mkv, de forma que podemos ver cuanto ocupa cada pista, tanto de audio como de video o subtitulos.

El script funciona con ffmpeg, que debera estar en el sistema, se puede descargar desde https://www.ffmpeg.org/download.html.

Si tenemos ffmpeg en el PATH del sistema, no hara falta modificar el script, si no debemos poner la ruta en el script...

![imagen](https://github.com/user-attachments/assets/94f0ab08-7b3d-47b0-a4a3-5d0f14a411a6)


El funcionamiento es sencillo, ejecutamos el script y le damos la ruta del mkv, pulsamos intro y analizara el fichero, mostrando los resultados por pantalla.

![imagen](https://github.com/user-attachments/assets/83f66363-cc7d-4ef9-a9ec-a3ae6fc6712e)


Si da error en la libreria colorama, podemos instalarla con `pip install colorama`
