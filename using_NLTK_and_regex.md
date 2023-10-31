# python coding
## Using NLTK
NLTK (Natural Language Toolkit) is a popular Python library for natural language processing (NLP). Here are some of the main things you can do with NLTK in Python:
Text processing: Perform operations like tokenization, stemming, lemmatization, part-of-speech tagging, parsing, named entity recognition etc. on text data.
Classification: Build text classifiers to categorize and label text data based on its contents. Common tasks include sentiment analysis, topic modeling etc.
Language detection: Identify the language that a given text is written in.
Corpora: Leverage the many text/language corpora included in NLTK like WordNet, Brown corpus, movie reviews etc. for tasks like word sense disambiguation.
Vocabulary: Build word frequency distributions, n-gram models to analyze word/phrase usage.
Concordancing: Generate concordances which show words in context to analyze patterns in text.
Parsing: Use NLTK's parsers to generate parse trees to analyze syntax and structure of sentences.
Similarity: Measure similarity between texts using metrics like cosine similarity, Jaccard similarity etc.
Generation: Build language generators for tasks like machine translation, summarization, question answering etc.
So in summary, NLTK provides a comprehensive suite of tools for common NLP tasks like preprocessing, classification, parsing etc. that can help with text analysis and language processing in Python.
## Using regex
The re module in Python is used for working with regular expressions. Regular expressions are a sequence of characters that form a search pattern. They can be used to check if a string contains the specified search pattern, find all occurrences of a pattern in a string, replace a pattern, etc. Here are some common functions in the re module:
re.search(pattern, string): Searches the string for a match, and returns the first match object found.
re.findall(pattern, string): Returns a list of all matches.
re\\.compile(pattern): Compiles a regular expression pattern into a regular expression object, which can be used for matching using its methods like search(), match(), findall(), split() etc.
re.sub(pattern, repl, string): Replaces all occurrences of the pattern in the string with the replacement string repl.
re.split(pattern, string): Splits the string by the occurrences of the pattern.
