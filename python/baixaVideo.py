from os import system, name
import os
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress

#definindo o diretório
diretorio_base = os.path.abspath(os.path.dirname(__file__))
local_salvar = os.path.join(diretorio_base, '..', 'midia')

def limpaTela():
    '''
    Limpa a tela de acordo com o sistema operacional
    '''
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

def MenuPrincipal():
    limpaTela()
    print("#"*50)
    print("1. Vídeo")
    print("2. Audio")
    print("3. Playlist")
    print("9. Sair")
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
                ys.download(output_path=local_salvar)
                print("\nVídeo baixado com sucesso\n")

            case 2:
                url = input("Digite a url: ")
                #Para baixar o audio
                yt = YouTube(url, on_progress_callback=on_progress)
                print(yt.title)
                ys = yt.streams.get_audio_only()
                ys.download(output_path=local_salvar)
                print("\nAudio baixado com sucesso\n")
        
            case 3:
                url = input("Digite a url: ")
                pl = Playlist(url)
                for video in pl.videos:
                    ys = video.streams.get_audio_only()
                    ys.download(output_path=local_salvar)
                print("\nPlaylist baixada com sucesso\n")

            case 9:
                print("Tchau :/")
                break;
            case _:
                print("Não é uma opção válida")
        
if __name__ == "__main__":
    main()