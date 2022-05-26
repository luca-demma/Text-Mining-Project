import time
from yaspin import yaspin
from yaspin.spinners import Spinners
import json


def read_file_to_json(file_path):
	file = open(file_path)
	data = json.load(file)
	return data


def write_json_to_file(json_to_write, name):
	path = './data/' + name
	os.makedirs(os.path.dirname(path), exist_ok=True)
	out_file = open(path, 'w')
	json.dump(json_to_write, out_file, indent=4)
	out_file.close()