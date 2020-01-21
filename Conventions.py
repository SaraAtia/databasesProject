EASY_GAME_CODE = "EASY"
HARD_GAME_CODE = "HARD"
CHALLENGING_GAME_CODE = "CHALLENGING"
EMPTY_ANSWERS_LIST_CODE = -1
VALID_ANSWERS_LIST_SIZE = 4
VALID_SONGS_ANSWERS_LIST_SIZE = 3
CRASHING_MODE = "CRASH"
WORKING_MODE = "WORKING_SERVER"

# LISTS
LIST_BEGINNING_OFF_SET = 0

# PROPERTIES STRINGS
ARTIST_NAME_STR = "Artist name: "
ORIGINS_STR = "From: "
BIRTH_DATE_STR = "Born on: "
SONG_NAME_STR = "Song "

# NUMBERS
ZERO = 0

# ---------- GAME LOGIC DEFINITIONS ---------
FROM = 'from'
GENRE = 'genre'
BIRTH_DATE = 'birth_date'
SIMILAR = 'similar'
NAME = 'name'
EMPTY_SONGS_LIST_STR = 'No songs this time!'
QUESTION_NAME_OFFSET = 'text'
RAW_ARTISTS_DATA_ARTIST_OFFSET = 'Artist'

ARTIST_NAME = "artist_name"
PROPERTIES = "properties"
QUESTIONS = "questions"


POINTS_TO_ADD = {
    EASY_GAME_CODE: 50,
    HARD_GAME_CODE: 70,
    CHALLENGING_GAME_CODE: 50
}

GAME_TYPES_CODE_FROM_VIEW_TO_STRING = {
    1: EASY_GAME_CODE,
    2: HARD_GAME_CODE,
    3: CHALLENGING_GAME_CODE
}


MOCK_GAME_SCORE = 1200

LIST_OF_ORIGINS = [
        "Israel",
        "Turkey",
        "Gibraltar",
        "Côte d'Ivoire",
        "Bosnia and Herzegovina",
        "Colombia",
        "Bulgaria",
        "Morocco",
        "Poland",
        "Russian Federation",
        "Guinea",
        "Marshall Islands",
        "Brunei Darussala",
        "Ireland",
        "Albania",
        "Finland",
        "Sweden",
        "Martinique",
        "Lithuania",
        "Benin",
        "Bangladesh"
    ]

NAME_OFF_SET = 0
GENDER_OFF_SET = 1
FROM_OFF_SET = 2
BIRTH_DATE_OFF_SET = 3
SONGS_LIST_OFF_SET = 4
PLAYING_ARTIST_OFF_SET = 0

NUMBER_OF_ORIGINS = 3


GAME_TYPES = [
    "EASY",
    "HARD",
    "CHALLENGING"
]

PREFERENCES_EXIST_STATUS = 1
PREFERENCES_NON_EXISTING = 0
USER_DOESNT_EXIST = -1
ADD_FAILURE = -1

QUESTIONS_DICT_NAME = "Name"
QUESTIONS_DICT_GENRE = "Genre"
QUESTIONS_DICT_BIRTH_DATE = "Birth_Date"
QUESTIONS_DICT_FROM = "From"
QUESTIONS_DICT_SONGS = "Songs"

QUESTIONS_STRINGS_DICT = {
    QUESTIONS_DICT_NAME: "What was the artist's name",
    QUESTIONS_DICT_GENRE: "Which of the following was one of the artist's genres?",
    QUESTIONS_DICT_BIRTH_DATE: "When was the artist born?",
    QUESTIONS_DICT_FROM: "Where was the artist from?",
    QUESTIONS_DICT_SONGS: "Which of the following songs belong to the artist?"
}