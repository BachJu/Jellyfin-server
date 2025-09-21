from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
import os

#definindo o diretório
diretorio_base = os.path.abspath(os.path.dirname(__file__))
local_salver = os.path.join(diretorio_base, '..', 'midia')

def MenuPrincipal():
    print("#"*50)
    print("1. Vídeo")
    print("2. Audio")
    print("3. Playlist")
    print("-"*50)
    print("#"*50)

def main():
    MenuPrincipal()
    while(True):
        match(int(input("Opcao: "))):
            case 1:
                url = input("Digite a url: ")
                #Para baixar o vídeo
                yt = YouTube(url, on_progress_callback=on_progress)
                print(yt.title)
                ys = yt.streams.get_highest_resolution()
                ys.download(output_path=local_salver)
                print("\nVídeo baixado com sucesso")

            case 2:
                url = input("Digite a url: ")
                #Para baixar o audio
                yt = YouTube(url, on_progress_callback=on_progress)
                print(yt.title)
                ys = yt.streams.get_audio_only()
                ys.download()
                print("\nAudio baixado com sucesso")
        
            case 3:
                url = input("Digite a url: ")
                pl = Playlist(url)
                for video in pl.videos:
                    ys = video.streams.get_audio_only()
                    ys.download()
                print("\nPlaylist baixada com sucesso")
            case 9:
                print("Tchau :/")
                break;
            case _:
                print("Não é uma opção válida")
        

m = main()