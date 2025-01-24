import os
import pandas as pd

def process_set(train_set_path, cropped_aligned_path, output_path):
    # Cria o diretório de saída, se não existir
    os.makedirs(output_path, exist_ok=True)
    
    # Itera sobre todos os arquivos txt na pasta Train_Set
    for txt_file in os.listdir(train_set_path):
        if txt_file.endswith('.txt'):
            video_name = os.path.splitext(txt_file)[0]  # Nome do vídeo sem extensão
            
            txt_file_path = os.path.join(train_set_path, txt_file)
            video_frame_path = os.path.join(cropped_aligned_path, video_name)
            
            # Verifica se a subpasta do vídeo correspondente existe
            if not os.path.exists(video_frame_path):
                print(f"Subpasta para {video_name} não encontrada em {cropped_aligned_path}. Pulando...")
                continue
            
            # Lê o arquivo txt e ignora o cabeçalho
            data = pd.read_csv(txt_file_path, delimiter=',')
            
            # Valida se há colunas esperadas no txt
            if 'valence' not in data.columns or 'arousal' not in data.columns:
                print(f"Arquivo {txt_file} não possui as colunas esperadas. Pulando...")
                continue
            
            # Verifica frames na pasta cropped_aligned
            frame_files = sorted([f for f in os.listdir(video_frame_path) if f.endswith('.jpg')])
            
            # Cria o CSV com as colunas desejadas
            output_data = []
            for idx, frame_file in enumerate(frame_files):
                # Verifica se o índice da linha corresponde a um frame
                if idx < len(data):
                    frame_id = os.path.splitext(frame_file)[0]  # ID do frame sem extensão
                    valence = data.iloc[idx]['valence']
                    arousal = data.iloc[idx]['arousal']
                    img_path = f"{video_name}/{frame_file}"
                    output_data.append([img_path, valence, arousal, frame_id])
            
            # Se houver dados para salvar, cria o CSV
            if output_data:
                output_csv_path = os.path.join(output_path, f"{video_name}.csv")
                output_df = pd.DataFrame(output_data, columns=['img', 'V', 'A', 'frame_id'])
                output_df.to_csv(output_csv_path, index=False)
                print(f"CSV criado para {video_name}: {output_csv_path}")

# Configurações de diretórios
train_set_path = r'G:\AffWild2\Annotations\VA_Estimation_Challenge\Train_Set\\'  # Diretório dos arquivos txt
cropped_aligned_path = r'G:\AffWild2\cropped\cropped_aligned\\'  # Diretório das subpastas de frames
output_path = r'G:\AffWild2\Annotations\preprocessed_VA_annotations\Train_Set\\'  # Diretório onde os CSVs serão salvos

# Executa o processamento
process_set(train_set_path, cropped_aligned_path, output_path)

train_set_path = r'G:\AffWild2\Annotations\VA_Estimation_Challenge\Validation_Set\\'  # Diretório dos arquivos txt
cropped_aligned_path = r'G:\AffWild2\cropped\cropped_aligned\\'  # Diretório das subpastas de frames
output_path = r'G:\AffWild2\Annotations\preprocessed_VA_annotations\Val_Set\\'  # Diretório onde os CSVs serão salvos

# Executa o processamento
process_set(train_set_path, cropped_aligned_path, output_path)
