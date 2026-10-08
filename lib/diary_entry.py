class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.progress = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        if len(self.contents) > 0:
            return len(self.contents.split())
        else:
            return 0

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return self.count_words()/wpm

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        if self.progress >= self.count_words(): #check if we have previouslt already reached end of text
            self.progress = 0 #if not set progress to start of text
        last_word = wpm * minutes + self.progress #calculates position of final word by adding number of words readable to current progress
        #for word in self.contents.split()[self.progress:last_word]:#for each word between progress and last word, add that word to the chunk string.
        chunk = self.contents.split()[self.progress:last_word] #previously for looped this and added to string, but this is simpler
        self.progress += last_word - self.progress #Calculate change in progress by the difference between last word and previous progress. Note can result over length of text, but covered by line 46
        return " ".join(chunk)
