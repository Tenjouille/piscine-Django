from path import Path

def	my_program():
	path = Path.cwd() / "new_folder"
	unique = 1
	new_path = path
	while new_path.exists():
		new_path = Path(str(path) + f"({unique})")
		unique += 1
	new_path.mkdir()
	with open(new_path / "new_file.txt", "w+") as f:
		f.write("something")
		f.seek(0)
		print(f.read())

if __name__ == "__main__":
	my_program()