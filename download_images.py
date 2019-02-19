import requests
from pathlib import Path
import os
import pandas as pd
import argparse


def download_img(url):
	img = requests.get(url)
	return img.content

def save_img(path, name, view_name, img):
	name_path = Path(path)/name
	name_path.mkdir(exist_ok=True)
	with open(name_path/(view_name + ".jpg"), 'wb') as f:
		f.write(img)


def create_label_dirs(root_dir, labels):
	root_dir = Path(root_dir)
	root_dir.mkdir(exist_ok=True)
	for label in labels:
		(root_dir/label).mkdir(exist_ok=True)


if __name__ == '__main__':
	root_dir = "./images_data/"
	csv_name = "./data/data-links.csv"
	img_data_df = pd.read_csv(csv_name)
	img_data_df['id'] = img_data_df['id'].str[0:-4]

	create_label_dirs(root_dir, img_data_df['class'].unique().tolist())

	parser = argparse.ArgumentParser(description="Footwear Image data download")
	parser.add_argument('-c', '--cont', action="store_true", help="Continue downloading?")
	args = parser.parse_args()


	if args.cont:
		img_ids = []
		for label_dir in Path(root_dir).iterdir():
			for img_dir in label_dir.iterdir():
				img_ids.append(img_dir.name)

		img_data_df.drop(img_data_df[img_data_df['id'].isin(img_ids)].index, inplace=True)

		print("continue downloading...")
	else:
		print("downloading from scratch...")

	for i, r in img_data_df.iterrows():
		for i in range(1, 6):
			view_name = 'view_' + str(i)
			url = r[view_name]
			try:
				img = download_img(r[view_name])
				save_img(root_dir + r['class'], r['id'], view_name, img)
			except:
				pass