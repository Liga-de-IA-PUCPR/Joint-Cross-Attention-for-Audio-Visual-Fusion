o pré-processamento foi criado e adaptado do pré-processamento fornecido no código do arquivo do Praveen:
https://github.com/praveena2j/Joint-Cross-Attention-for-Audio-Visual-Fusion?tab=readme-ov-file#Table_of_Content
então é possível ter uma ideia dos passos pelo README fornecido por ele, porém os códigos não rodam de primeira, por isso adaptei esses scripts.

Passo 1 - Baixar a base do AffWild2
	Na pasta Video_files estão os arquivos brutos, eles são usados para extrair as faces e os arquivos de audio.
	O dataset ja fornece as faces cortadas para ganhar tempo, esses arquivos de cada vídeo, frame a frame estão na pasta cropped

Passo 2 - Préprocessar imagens (vídeo)
	Se usar os arquivos cortados fornecidos com a base pode pular essa etapa

Passo 3 - Préprocessar audio
	Essa etapa é demorada, a ideia é que para cada frame de cada vídeo, um pedaço de audio correspondente deve ser cortado do arquivo bruto.
	Executar o script preprocess_audio.py, alterando os paths para as pastas desejadas.

Passo 4 - Préprocessar labels
	Nas Annotation files são fornecidos txts que contém o nome de cada vídeo, e cada linha corresponde a 1 frame do vídeo.
	Para gerar os labels no formato correto (['img', 'V', 'A', 'frame_id']) é preciso executar o arquivo gerar_labels.py.
	Esse script foi criado e adaptado do fornecido pelo Praveen, a ideia é que na pasta VA_estimation_challenge existem arquivos txt contento VA para train_set e val_set.
	O que você deve fazer é organizar os arquivos dessas pastas de acordo com o que deseja usar de train_set e val_set, e se necessário criar uma pasta text_set e colocar os arquivos txt fonte de VA nas pastas correspondentes.
	Esse script criará uma pasta preprocessed_VA_annotations com os arquivos CSV no formato usado:
	img,V,A,frame_id
		1-30-1280x720/00001.jpg,0.148,0.352,00001
		1-30-1280x720/00002.jpg,0.148,0.36,00002
		1-30-1280x720/00003.jpg,0.148,0.362,00003
		1-30-1280x720/00004.jpg,0.148,0.36,00004
		1-30-1280x720/00005.jpg,0.148,0.357,00005
		1-30-1280x720/00006.jpg,0.148,0.355,00006
		1-30-1280x720/00007.jpg,0.148,0.353,00007
		1-30-1280x720/00008.jpg,0.148,0.355,00008


Caso eu possa te ajudar a tirar alguma dúvida me mande um email: victorschnepper@gmail.com


