import pandas as pd
import os
import sys
#anno_path = "/misc/lu/fast_scratch/patx/rajasegp/Affwild2/Annotations"
anno_path = r'G:\AffWild2\Annotations'

def produce_multi_task_videos():
	train_videos = os.listdir(os.path.join(anno_path, "VA_Estimation_Challenge", "Train_Set"))
	val_videos = os.listdir(os.path.join(anno_path, "VA_Estimation_Challenge", "Validation_Set"))
	test_videos = os.listdir(os.path.join(anno_path, "VA_Estimation_Challenge", "TestSet"))

	train_videos = list(set(train_videos))
	val_videos = list(set(val_videos))
	return train_videos,val_videos

train_videos,val_videos = produce_multi_task_videos()


def get_names(id):
	name = ""
	if id>=0 and id<10:
		name = "0000" + str(id)
	elif id>=10 and id<100:
		name = "000" + str(id)
	elif id>=100 and id<1000:
		name = "00" + str(id)
	elif id>=1000 and id<10000:
		name = "0" + str(id)
	else:
		name = str(id)
	return name

def produce_va_labels_for_one_video(video_name, flag):
	label_dict = {}

	f = open(os.path.join(anno_path,"VA_Estimation_Challenge",flag,video_name))
	lines = f.readlines()[1:]
	for i in range(len(lines)):
		l = lines[i].strip().split(",")
		if l[0] == "-5" or l[1] == "-5":
			print(l)
			continue
		frame = get_names(i+1)
		#if os.path.exists(os.path.join(img_path,video_name,frame+".jpg")):
		n = video_name.split(".")[0]+"/"+frame+".jpg"
		if n not in label_dict.keys():
			label_dict[n] = [float(l[0]),float(l[1]), frame]
		else:
			label_dict[n][0] = float(l[0])
			label_dict[n][1] = float(l[1])
			label_dict[n][2] = float(frame)
	return label_dict


def produce_anno_csvs(videos, flag):
	#save_path = "/misc/lu/fast_scratch/patx/rajasegp/Affwild2/Annotations/preprocessed_VA_annotations/" + flag
	save_path = r'G:\AffWild2\Annotations\preprocessed_VA_annotations\\' + flag
	if not os.path.isdir(save_path):
		os.makedirs(save_path)
	for video in videos:
		label_dict = produce_va_labels_for_one_video(video, flag)
		data = pd.DataFrame()
		imgs,V,A,frame_id = [],[],[],[]
		for k,v in label_dict.items():
			imgs.append(k)
			V.append(v[0])
			A.append(v[1])
			frame_id.append(v[2])
		data["img"],data["V"],data["A"], data["frame_id"] = imgs,V,A, frame_id
		data.to_csv(os.path.join(save_path,video.split(".")[0]+".csv"))




print(train_videos)
print(len(train_videos))
print(val_videos)
print(len(val_videos))
produce_anno_csvs(train_videos, 'Train_Set')
#produce_anno_csvs(val_videos, 'Val_Set')

#produce_training_data()
#produce_category_csvs()
#produce_total_csvs()
#### for train and val
#count = 0
#video_data = [[train_videos, 'Train_Set'], [val_videos, 'Validation_Set']]
#for videos in video_data:
	#produce_anno_csvs(videos[0], videos[1])
##    flag = ['Train_Set', 'Val_Set']
##produce_anno_csvs(val_videos, 'Val_Set')

#anno_path = '/misc/lu/fast_scratch/patx/rajasegp/Affwild2/Annotations/VA_Estimation_Challenge/TestSet/names_of_videos_in_each_test_set/Valence_Arousal_Estimation_Challenge_test_set_release.txt'
#anno_path = r'G:\AffWild2\Annotations\VA_Estimation_Challenge\TestSet\names_of_videos_in_each_test_set\Valence_Arousal_Estimation_Challenge_test_set_release.txt'
label_dict = {}
#test_annot_path = "/misc/lu/fast_scratch/patx/rajasegp/Affwild2/Annotations/preprocessed_VA_annotations/Test_Set/"

test_annot_path = 'G:\\AffWild2\\Annotations\\preprocessed_VA_annotations\\TestSet\\'

