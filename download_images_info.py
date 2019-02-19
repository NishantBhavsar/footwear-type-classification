from pathlib import Path
import pandas as pd

root_dir = "./images_data/"
csv_name = "./data/data-links.csv"
img_data_df = pd.read_csv(csv_name)
img_data_df['id'] = img_data_df['id'].str[0:-4]


total_info = {'label_dir_count': 0, 'total_imgs': 0, 'total_imgs_view': 0, 'view_1': 0, 'view_2': 0, 'view_3': 0, 'view_4': 0,'view_5': 0}
for label_dir in Path(root_dir).iterdir():
	total_info['label_dir_count'] += 1
	imgs_info = {'img_dir_count': 0, 'view_1': 0, 'view_2': 0, 'view_3': 0, 'view_4': 0,'view_5': 0}
	
	print("Label: ", label_dir.name)
	
	for img_dir in label_dir.iterdir():
		imgs_info['img_dir_count'] += 1
		for img in img_dir.iterdir():
			imgs_info[img.name[0:-4]] += 1

	total_imgs_views = (imgs_info['view_1'] + imgs_info['view_2'] + imgs_info['view_3'] + imgs_info['view_4'] + imgs_info['view_5'])
	print("========================================")
	print("Total images: ", imgs_info['img_dir_count'])
	print("Total images with all views: ", total_imgs_views)
	print("Total view 1 images: ", imgs_info['view_1'])
	print("Total view 2 images: ", imgs_info['view_2'])
	print("Total view 3 images: ", imgs_info['view_3'])
	print("Total view 4 images: ", imgs_info['view_4'])
	print("Total view 5 images: ", imgs_info['view_5'])

	total_info['total_imgs'] += imgs_info['img_dir_count']
	total_info['total_imgs_view'] += total_imgs_views
	total_info['view_1'] += imgs_info['view_1']
	total_info['view_2'] += imgs_info['view_2']
	total_info['view_3'] += imgs_info['view_3']
	total_info['view_4'] += imgs_info['view_4']
	total_info['view_5'] += imgs_info['view_5']

	print("\n\n")

print("============== ALL INFO =============")
for key, val in total_info.items():
	print(key, ": ", val)




