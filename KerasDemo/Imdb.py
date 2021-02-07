from keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10_000)

# Slovniky pro kodovani a dekodovani
word_index = imdb.get_word_index()
inveres_word_index = dict([(value, key) for (key, value) in word_index.items()])
decoded = " ".join([inveres_word_index.get(i - 3, "?") for i in train_data[0]])
# print("Decode:", decoded)
