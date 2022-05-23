import time
from yaspin import yaspin
from yaspin.spinners import Spinners
import json


def read_file_to_json(file_path):
	with yaspin(Spinners.point, text="READING DATA FROM FILE") as spinner:
		file = open(file_path)
		data = json.load(file)
		spinner.ok("SUCCESS ✅: ")
		return data


def write_json_to_file(json_to_write, name):
	with yaspin(Spinners.point, text="WRITING DATA TO FILE: " + name) as spinner:
		out_file = open('./data/' + name, 'w')
		json.dump(json_to_write, out_file, indent=4)
		out_file.close()
		spinner.ok("SUCCESS ✅: ")
