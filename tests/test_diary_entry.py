from lib.diary_entry import *

#When properties Title and Contents are set on init
#Format returns the title and contents as a string seperated by a colon
def test_diary_entry_format_returns_set_properties():
    entry = DiaryEntry("Title", "Many words make a story")
    result = entry.format()
    assert result == "Title: Many words make a story"

#When count_words is called
#Returns the number of words in contents
def test_diary_entry_count_words_returns_num_words_in_entry():
    entry = DiaryEntry("Asbestos", "All these science spheres are made of asbestos, by the way. Keeps out the rats.")
    result = entry.count_words()
    assert result == 15

#When count_words is called on empty content
#Returns 0 (note: should we raise error instead?)
def test_diary_entry_count_words_returns_zero_for_empty_content():
    entry = DiaryEntry("Black Mesa Merits", "")
    result = entry.count_words()
    assert result == 0

#When reading_time is called on with wpm equal to number of words
#Return 1
def test_diary_entry_reading_time_returns_1_for_10_words_10_wpm():
    entry = DiaryEntry("Questions to Cave", "What was in that phonebook of a contract I signed?")
    result = entry.reading_time(10)
    assert result == 1

#When reading_time is called with non-1 resulting values
#Returns correct division result
def test_diary_entry_reading_time_returns_100_for_2000_words_20_wpm():
    entry = DiaryEntry("Lemons", f"{"lemons "*2000}")
    result = entry.reading_time(20)
    assert result == 100

#When reading_chunk is called with values to read whole contents
#Returns string with whole contents
def test_diary_entry_reading_chunk_returns_10_words_for_10_wpm_1_minute():
    entry = DiaryEntry("Questions to Cave", "What was in that phonebook of a contract I signed?")
    result = entry.reading_chunk(10,1)
    assert result == "What was in that phonebook of a contract I signed?"

#When reading_chunk is called twice whilst text is not complete
#Second call returns text starting from the point the first call ended
def test_diary_entry_reading_chunk_continues_along_text_after_sequential_calls():
    entry = DiaryEntry("Introduction", "Greetings, friend. I'm Cave Johnson, CEO of Aperture Science. You might know us as a vital participant in the 1968 senate hearings on missing astronauts. And you've most likely used one of the many products we invented, but that other people have somehow managed to steal from us. Black Mesa can eat my bankrupt-...")
    entry.reading_chunk(2,1)
    result = entry.reading_chunk(3,1)
    assert result == "I'm Cave Johnson,"

#When reading_chunk is called after a previous call has finished the text
#Returns text from start of contents
def test_diary_entry_reading_chunk_continues_from_start_when_called_after_finishing_text():
    entry = DiaryEntry("Asbestos Part Two","Let us know if you feel a shortness of breath, a persistant dry cough or your heart stopping. Because that's not part of the test. That's asbestos")
    entry.reading_chunk(25,1)
    entry.reading_chunk(3,1)
    result = entry.reading_chunk(10,1)
    assert result == "Let us know if you feel a shortness of breath,"

#When reading chunk is called after finishing on the exact last word
#Returns text from start of contents
def test_diary_entry_reading_chunk_continues_from_start_when_called_after_exactly_last_word():
    entry = DiaryEntry("Asbestos Part Two","Let us know if you feel a shortness of breath, a persistant dry cough or your heart stopping. Because that's not part of the test. That's asbestos")
    entry.reading_chunk(25,1)
    entry.reading_chunk(2,1)
    result = entry.reading_chunk(10,1)
    assert result == "Let us know if you feel a shortness of breath,"