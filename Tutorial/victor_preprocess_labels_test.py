import os
import pandas as pd

# Caminhos
anno_path = r'G:\AffWild2\Annotations'
test_annot_path = r'G:\AffWild2\Annotations\preprocessed_VA_annotations\TestSet\\'

# Criar diretório se não existir
if not os.path.exists(test_annot_path):
    os.makedirs(test_annot_path)

# Lendo linhas do arquivo principal
with open(os.path.join(anno_path, 'VA_Estimation_Challenge', 'TestSet', 'names_of_videos_in_each_test_set', 'Valence_Arousal_Estimation_Challenge_test_set_release.txt'), 'r') as f:
    lines = f.readlines()

label_dict = {}

for line in lines:
    f_name = line.strip()
    vid_name = f_name.rstrip('_left').rstrip('_right')

    file_name = os.path.join('realtimestamps', vid_name + '_video_ts.txt')
    
    if not os.path.exists(file_name):
        print(f"Aviso: Arquivo {file_name} não encontrado. Pulando.")
        continue

    with open(file_name, 'r') as video_file:
        video_lines = video_file.readlines()[1:]

    for j, _ in enumerate(video_lines):
        frame = get_names(j + 1)
        n = os.path.join(f_name, frame + '.jpg')
        label_dict[n] = [frame]

data = pd.DataFrame.from_dict(label_dict, orient='index', columns=['frame_id'])
data.reset_index(inplace=True)
data.rename(columns={'index': 'img'}, inplace=True)

data.to_csv(os.path.join(test_annot_path, f"{f_name}.csv"), index=False)
