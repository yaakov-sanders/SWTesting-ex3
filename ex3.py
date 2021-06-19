import csv
import subprocess
import os, shutil

INPUT_FILE_PATH = "./images/input.csv"
OUTPUT_FOLDER_PATH = "./output"


def get_input_file(input_file_path):
	csv_file = None
	reader = None
	try:
		csv_file = open(input_file_path, 'r')
		reader = csv.DictReader(csv_file)
	except FileNotFoundError:
		print("Error: File not found")
	finally:
		return reader, csv_file

def make_output_folder():
	if not os.path.exists(OUTPUT_FOLDER_PATH):
		os.mkdir(OUTPUT_FOLDER_PATH)
	else:
		for filename in os.listdir(OUTPUT_FOLDER_PATH):
			file_path = os.path.join(OUTPUT_FOLDER_PATH, filename)
			try:
				if os.path.isfile(file_path) or os.path.islink(file_path):
					os.unlink(file_path)
				elif os.path.isdir(file_path):
					shutil.rmtree(file_path)
			except Exception as e:
				print('Failed to delete %s. Reason: %s' % (file_path, e))


if __name__ == "__main__":
	csv_dict, original_file = get_input_file(INPUT_FILE_PATH)
	make_output_folder()
	if csv_dict:
		for row in csv_dict:
			subprocess.run(["tesseract", row["Path"] + "/" + row["Filename"] , OUTPUT_FOLDER_PATH + "/" + row["Filename"] + ".txt"])
		original_file.close()
