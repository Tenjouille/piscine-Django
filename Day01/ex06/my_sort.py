def	my_sort():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	years : list = list(set(year for year in d.values()))
	years.sort()
	for year in years:
		same_year : list = []
		for musician in d:
			if d[musician] == year:
				same_year.append(musician)
		same_year.sort()
		for musician in same_year:
			print(musician)

if __name__ == "__main__":
	my_sort()