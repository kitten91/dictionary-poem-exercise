def word_count(file_name):
	poem_dictionary = {}
	poem = open(file_name)
	for line in poem:
		list_of_words = line.split()
		for word in line:
			word_count = poem_dictionary.get(word, 0) # used in place of if statement to find if a key is in the dictionary
			poem_dictionary[word] = word_count + 1 # add's 1 to the value if key exist in dictionary
			print poem_dictionary


	poem.close()

word_count("test.txt")
