import yt_dlp
import os

def descargar_audio_youtube(url, carpeta='Mi_audio_youtube'):
    try:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        print("Descargando audio de YouTube...")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print("Descarga completada.")

    except Exception as e:
        print(f"Ocurrió un error al descargar el audio: {e}")

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    descargar_audio_youtube(url)
