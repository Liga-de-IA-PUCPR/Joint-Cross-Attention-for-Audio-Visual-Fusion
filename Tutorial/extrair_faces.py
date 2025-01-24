import os
import subprocess
from pathlib import Path
import cv2

def resize_images(directory, target_resolution=(224, 224)):
    """
    Redimensiona todas as imagens em um diretório para a resolução especificada.
    
    Args:
        directory (Path): Caminho para o diretório contendo as imagens.
        target_resolution (tuple): Resolução alvo (largura, altura).
    """
    for image_file in directory.glob("*.png"):
        img = cv2.imread(str(image_file))
        if img is None:
            print(f"Erro ao carregar a imagem: {image_file}")
            continue
        resized_img = cv2.resize(img, target_resolution, interpolation=cv2.INTER_AREA)
        cv2.imwrite(str(image_file), resized_img)

def extract_frames_faces(source_path, output_path, openface_path="FeatureExtraction", resolution=(224, 224)):
    """
    Extrai frames e detecta faces de vídeos em um diretório usando OpenFace, 
    e redimensiona as imagens para a resolução especificada.
    
    Args:
        source_path (str): Caminho para o diretório com os vídeos.
        output_path (str): Caminho para o diretório onde os resultados serão salvos.
        openface_path (str): Caminho para o executável `FeatureExtraction` do OpenFace.
        resolution (tuple): Resolução desejada para as imagens (largura, altura).
    """
    source_path = Path(source_path)
    output_path = Path(output_path)
    
    # Criar o diretório de saída se não existir
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Verificar se o diretório de origem existe
    if not source_path.exists() or not source_path.is_dir():
        print(f"Erro: O caminho de origem {source_path} não existe ou não é um diretório.")
        return
    
    # Iterar sobre todos os vídeos no diretório de origem
    for video_file in source_path.glob("*.mp4"):
        video_name = video_file.stem  # Nome do arquivo sem extensão
        video_output_dir = output_path / video_name
        
        # Criar diretório para salvar as saídas do vídeo
        video_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Comando para executar o FeatureExtraction
        command = [
            openface_path,
            "-f", str(video_file),
            "-out_dir", str(video_output_dir)  # Extrações adicionais
        ]
        
        try:
            print(f"Processando: {video_file} -> {video_output_dir}")
            subprocess.run(command, check=True)
            
            # Redimensionar as imagens extraídas
            print(f"Redimensionando imagens em {video_output_dir} para {resolution}")
            resize_images(video_output_dir, resolution)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao processar o vídeo {video_file}: {e}")
        except FileNotFoundError:
            print("Erro: Certifique-se de que o caminho do `FeatureExtraction` está correto.")
    
    print("Processamento concluído.")

# Configuração
source_path = "G:/AffWild2/Data/Video_files"  # Altere para o caminho do diretório de entrada
output_path = "G:/AffWild2/cropped_new"   # Altere para o caminho do diretório de saída
openface_tool = "C:/OpenFace_2.2.0_win_x64/FeatureExtraction.exe"   # Caminho para o executável do OpenFace

# Executar
extract_frames_faces(source_path, output_path, openface_tool, resolution=(224, 224))
