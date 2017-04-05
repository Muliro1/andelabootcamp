def word_count(astring):
	wordCount = {}
	for ch in astring.split():
		if ch not in wordCount:
			wordCount[ch] = 1
		else:
			wordCount[ch] += 1
	return wordCount
