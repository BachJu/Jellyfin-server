from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress

def MenuPrincipal() -> int:
    opcoes = [1, 2, 3, 9]
    opcao = 10

    while opcao not in opcoes:
        print("#"*50)
        print("1. Vídeo")
        print("2. Audio")
        print("3. Playlist")
        print("-"*50)
        opcao = int(input("Opcao: "))
        print("#"*50)
    return opcao

def main():
    opcao = MenuPrincipal()
    while (opcao != 9):
        url = "url"

        if (opcao == 1):
            #Para baixar o vídeo
            yt = YouTube(url, on_progress_callback=on_progress)
            print(yt.title)
            ys = yt.streams.get_highest_resolution()
            ys.download()

        if (opcao == 2):
            #Para baixar o audio
            yt = YouTube(url, on_progress_callback=on_progress)
            print(yt.title)
            ys = yt.streams.get_audio_only()
            ys.download()
        
        if (opcao == 3):
            pl = Playlist(url)
            for video in pl.videos:
                ys = video.streams.get_audio_only()
                ys.download()

'''
#Diretório para salvar o vídeo/audio
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
ys.download(output_path="path/to/directory")
'''