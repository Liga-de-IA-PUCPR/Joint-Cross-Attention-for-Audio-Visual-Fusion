import os

def encontrar_indices_faltantes(video_files_dir, output_dir):
    # Obter a lista de vídeos e pastas
    video_files = sorted(os.listdir(video_files_dir))  # Ordena para garantir consistência
    video_files_bases = {os.path.splitext(v)[0] for v in video_files}  # Nomes sem extensão
    
    pastas = {folder for folder in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, folder))}
    
    # Identificar vídeos não processados
    nao_processados = video_files_bases - pastas
    
    # Obter índices dos vídeos não processados
    indices_nao_processados = [
        i for i, video in enumerate(video_files) if os.path.splitext(video)[0] in nao_processados
    ]
    
    return indices_nao_processados, nao_processados

# Caminhos dos diretórios
videos_dir = r'G:\AffWild2\Data\Video_files'
output_dir = r'G:\AffWild2\Data\SegmentedAudioFiles\Shift_1_win_32'

# Encontrar índices dos vídeos não processados
indices_faltantes, nao_processados = encontrar_indices_faltantes(videos_dir, output_dir)

# Exibir resultados
print("Índices dos vídeos não processados:", indices_faltantes)
print("Vídeos não processados:", nao_processados)
