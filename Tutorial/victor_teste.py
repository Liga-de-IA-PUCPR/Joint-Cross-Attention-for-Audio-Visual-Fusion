import os

def verificar_processamento(videos_dir, output_dir):
    # Obter nomes dos arquivos de vídeo (sem extensão) no diretório de entrada
    videos = {os.path.splitext(video)[0] for video in os.listdir(videos_dir) if os.path.isfile(os.path.join(videos_dir, video))}
    
    # Obter nomes das pastas no diretório de saída
    pastas = {folder for folder in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, folder))}
    
    # Verificar diferenças
    nao_processados = videos - pastas
    processados_extras = pastas - videos
    
    # Resultados
    if not nao_processados:
        print("Todos os vídeos foram processados.")
    else:
        print("Vídeos não processados:")
        for video in nao_processados:
            print(f"- {video}")
    
    if processados_extras:
        print("\nPastas que não correspondem a nenhum vídeo:")
        for pasta in processados_extras:
            print(f"- {pasta}")

# Caminhos dos diretórios
videos_dir = r'G:\AffWild2\Data\Video_files'
output_dir = r'G:\AffWild2\Data\SegmentedAudioFiles\Shift_1_win_32'

# Verificar
verificar_processamento(videos_dir, output_dir)
