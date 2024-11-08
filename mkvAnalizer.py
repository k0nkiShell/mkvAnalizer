import subprocess
import re
from colorama import Fore

# Ejecutamos ffmpeg y capturamos la salida
def get_ffmpeg_stream_info(file_path):
    # Comando que ejecuta ffmpeg para obtener información del archivo
    
    # Si no esta instalado ffmpeg en el PATH se puede usar directamente desde la ruta donde se encuentre ffmpeg.exe
    # command = ["C:\\ffmpeg\\bin\\ffmpeg.exe", "-i", file_path]
    
    # Si esta instalado lo llamamos directamente
    command = ["ffmpeg", "-i", file_path]
    
    # Ejecutamos el comando y obtenemos la salida
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)
    
    # Devolvemos la salida del stderr de ffmpeg (donde se muestra la información del archivo)
    return result.stderr

# Función para procesar y extraer la información de los streams (solo Audio/Video)
def extract_stream_info(output):
    # Lista de líneas que contendrán la información que queremos extraer
    filtered_lines = []
    
    # Dividir la salida en líneas
    lines = output.splitlines()
    
    # Variables para controlar si estamos dentro de un stream
    current_stream = None
    
    for line in lines:
        # Detectar información de streams de Video, Audio o Subtitulos
        if "Stream #" in line and ("Audio" in line or "Video" in line or "Subtitle" in line):
            current_stream = line.strip()
            filtered_lines.append(current_stream)
        
        # Buscar la duración del stream
        if "DURATION-eng    :" in line:
            match = re.search(r"DURATION-eng\s*:\s*(\d{2}:\d{2}:\d{2})", line)
            if match:
                duration = match.group(1)
                filtered_lines.append(f"      DURACION  : {Fore.BLUE}{duration}{Fore.RESET}")
                        
        # Buscar el tamaño en bytes de un stream
        if "NUMBER_OF_BYTES" in line:
            # Convertimos los bytes a MB para facilitar la lectura
            if current_stream:
                bytes_value = int(line.split(':')[1].strip())
                size_mb = bytes_value / (1024 * 1024)
                filtered_lines.append(f"      TAMAÑO    : {Fore.YELLOW}{size_mb:.2f} MB{Fore.RESET}")
                current_stream = None  # Reset para el próximo stream
    
    return filtered_lines

# Función principal
def main():
    file_path = input("Introduce la ruta al archivo MKV: ")
    
    # Obtener la salida de ffmpeg
    output = get_ffmpeg_stream_info(file_path)
    
    # Extraer la información relevante de los streams
    stream_info = extract_stream_info(output)
    
    # Imprimir la información formateada
    for info in stream_info:
        print(info)

    input("Presiona Enter para salir...")


if __name__ == "__main__":
    main()
