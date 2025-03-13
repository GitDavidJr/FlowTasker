import pyautogui as pa
import time


def clica(loc):
    try:
        localizacao = pa.locateOnScreen(f'img/{loc}.png', confidence=0.8)
        if localizacao:
            print(f"Botão encontrado em {localizacao}")  # Imprime as coordenadas
            pa.click(localizacao)
        else:
            print(f"Imagem '{loc}' não encontrada com confiança suficiente. Continuando execução.")
    except pa.ImageNotFoundException:
        print(f"Imagem '{loc}' não encontrada. Continuando execução.")
    except FileNotFoundError:
        print(f"Arquivo de imagem 'img/{loc}.png' não encontrado.")
        time.sleep(60)

def espera(loc, max_tentativas=1000):
    """
    Aguarda até que uma imagem específica apareça na tela.

    :param loc: Nome do arquivo de imagem (sem extensão) localizado na pasta 'img'.
    :param max_tentativas: Número máximo de tentativas antes de interromper o loop (padrão: 1000).
    """

    carregou = False
    tentativas = 0

    while not carregou:
        # Verifica se o limite de tentativas foi atingido
        if tentativas >= max_tentativas:
            print("Limite máximo de tentativas atingido.")
            break

        try:
            # Tenta localizar a imagem na tela
            localizacao = pa.locateOnScreen(f'img/{loc}.png', confidence=0.8)  # Ajuste o confidence se necessário

            if localizacao:
                print(f"Carregado na posição {localizacao}")
                carregou = True
            else:
                time.sleep(0.5)  # Aguarda antes de tentar novamente
                tentativas += 1

        except FileNotFoundError:
            print(f"Erro: Arquivo de imagem 'img/{loc}.png' não encontrado.")
            break
        except pa.ImageNotFoundException:
            print(f"Erro: A imagem 'img/{loc}.png' não foi encontrada na tela.")
            time.sleep(0.5)
            tentativas += 1
    
    return carregou
