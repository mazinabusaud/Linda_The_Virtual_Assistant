#Mazin Abusaud
#Spring 2022
#CSCI490 Capstone Project
#Linda the Desktop Assistant

from cgitb import text
from hashlib import new
from re import sub
from turtle import speed
from unittest import skip
from winsound import PlaySound
import shutil
# from translate import Translator
import speech_recognition #used for speech recognition
import pyaudio #used to allow speech_recognition to audio directly from mic
import gtts #google text to speech
import requests, json #used from API calls
import os
import subprocess #used to launch prograns
import platform
from playsound import playsound #used to talk back
import spotipy #used for the spotify API
from spotipy.oauth2 import SpotifyOAuth #Used for spotify API user authentication
import psutil
import random
import time
import sports
import keyboard
import multiprocessing as mp
from googletrans import Translator
import webbrowser #used to perform google searches

recognizer = speech_recognition.Recognizer()
recognizer.energy_threshold = 100
weather_url = "https://api.openweathermap.org/data/2.5/weather?"
weather_api_key = "insert_here"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="insert_here",
                                               client_secret="insert_here",
                                               redirect_uri="https://www.google.com/",
                                               scope="user-modify-playback-state user-read-currently-playing user-read-playback-state"))

listening_responses = ["yes?","mhmm?","Okay, I am listening", "What would you like help with?"]
invalid_responses = ["That's not a valid command.","I'm sorry, I don't recognize that command.","Hmm, I don't know that command."]

default_lang = 'en'
languages = {
    'aa': 'Afar',
    'ab': 'Abkhazian',
    'af': 'Afrikaans',
    'ak': 'Akan',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'an': 'Aragonese',
    'hy': 'Armenian',
    'as': 'Assamese',
    'av': 'Avaric',
    'ae': 'Avestan',
    'ay': 'Aymara',
    'az': 'Azerbaijani',
    'ba': 'Bashkir',
    'bm': 'Bambara',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bh': 'Bihari languages',
    'bi': 'Bislama',
    'bo': 'Tibetan',
    'bs': 'Bosnian',
    'br': 'Breton',
    'bg': 'Bulgarian',
    'my': 'Burmese',
    'ca': 'Catalan; Valencian',
    'cs': 'Czech',
    'ch': 'Chamorro',
    'ce': 'Chechen',
    'zh': 'Chinese',
    'cu': 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic',
    'cv': 'Chuvash',
    'kw': 'Cornish',
    'co': 'Corsican',
    'cr': 'Cree',
    'cy': 'Welsh',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'dv': 'Divehi; Dhivehi; Maldivian',
    'nl': 'Dutch; Flemish',
    'dz': 'Dzongkha',
    'el': 'Greek: Modern 1453-',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'eu': 'Basque',
    'ee': 'Ewe',
    'fo': 'Faroese',
    'fa': 'Persian',
    'fj': 'Fijian',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Western Frisian',
    'ff': 'Fulah',
    'Ga': 'Georgian',
    'de': 'German',
    'gd': 'Gaelic; Scottish Gaelic',
    'ga': 'Irish',
    'gl': 'Galician',
    'gv': 'Manx',
    'el': 'Greek: Modern 1453-',
    'gn': 'Guarani',
    'gu': 'Gujarati',
    'ht': 'Haitian; Haitian Creole',
    'ha': 'Hausa',
    'he': 'Hebrew',
    'hz': 'Herero',
    'hi': 'Hindi',
    'ho': 'Hiri Motu',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'hy': 'Armenian',
    'ig': 'Igbo',
    'is': 'Icelandic',
    'io': 'Ido',
    'ii': 'Sichuan Yi; Nuosu',
    'iu': 'Inuktitut',
    'ie': 'Interlingue; Occidental',
    'ia': 'Interlingua International Auxiliary Language Association',
    'id': 'Indonesian',
    'ik': 'Inupiaq',
    'is': 'Icelandic',
    'it': 'Italian',
    'jv': 'Javanese',
    'ja': 'Japanese',
    'kl': 'Kalaallisut; Greenlandic',
    'kn': 'Kannada',
    'ks': 'Kashmiri',
    'ka': 'Georgian',
    'kr': 'Kanuri',
    'kk': 'Kazakh',
    'km': 'Central Khmer',
    'ki': 'Kikuyu; Gikuyu',
    'rw': 'Kinyarwanda',
    'ky': 'Kirghiz; Kyrgyz',
    'kv': 'Komi',
    'kg': 'Kongo',
    'ko': 'Korean',
    'kj': 'Kuanyama; Kwanyama',
    'ku': 'Kurdish',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'li': 'Limburgan; Limburger; Limburgish',
    'ln': 'Lingala',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish; Letzeburgesch',
    'lu': 'Luba-Katanga',
    'lg': 'Ganda',
    'mk': 'Macedonian',
    'mh': 'Marshallese',
    'ml': 'Malayalam',
    'mi': 'Maori',
    'mr': 'Marathi',
    'ms': 'Malay',
    'Mi': 'Micmac',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'mt': 'Maltese',
    'mn': 'Mongolian',
    'mi': 'Maori',
    'ms': 'Malay',
    'my': 'Burmese',
    'na': 'Nauru',
    'nv': 'Navajo; Navaho',
    'nr': 'Ndebele: South; South Ndebele',
    'nd': 'Ndebele: North; North Ndebele',
    'ng': 'Ndonga',
    'ne': 'Nepali',
    'nl': 'Dutch; Flemish',
    'nn': 'Norwegian Nynorsk; Nynorsk: Norwegian',
    'nb': 'Bokmål: Norwegian; Norwegian Bokmål',
    'no': 'Norwegian',
    'oc': 'Occitan post 1500',
    'oj': 'Ojibwa',
    'or': 'Oriya',
    'om': 'Oromo',
    'os': 'Ossetian; Ossetic',
    'pa': 'Panjabi; Punjabi',
    'fa': 'Persian',
    'pi': 'Pali',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ps': 'Pushto; Pashto',
    'qu': 'Quechua',
    'rm': 'Romansh',
    'ro': 'Romanian; Moldavian; Moldovan',
    'ro': 'Romanian; Moldavian; Moldovan',
    'rn': 'Rundi',
    'ru': 'Russian',
    'sg': 'Sango',
    'sa': 'Sanskrit',
    'si': 'Sinhala; Sinhalese',
    'sk': 'Slovak',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'se': 'Northern Sami',
    'sm': 'Samoan',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'so': 'Somali',
    'st': 'Sotho: Southern',
    'es': 'Spanish',
    'sq': 'Albanian',
    'sc': 'Sardinian',
    'sr': 'Serbian',
    'ss': 'Swati',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'ty': 'Tahitian',
    'ta': 'Tamil',
    'tt': 'Tatar',
    'te': 'Telugu',
    'tg': 'Tajik',
    'tl': 'Tagalog',
    'th': 'Thai',
    'bo': 'Tibetan',
    'ti': 'Tigrinya',
    'to': 'Tonga Tonga Islands',
    'tn': 'Tswana',
    'ts': 'Tsonga',
    'tk': 'Turkmen',
    'tr': 'Turkish',
    'tw': 'Twi',
    'ug': 'Uighur; Uyghur',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'uz': 'Uzbek',
    've': 'Venda',
    'vi': 'Vietnamese',
    'vo': 'Volapük',
    'cy': 'Welsh',
    'wa': 'Walloon',
    'wo': 'Wolof',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zh': 'Chinese',
    'zu': 'Zulu'
}

#used for retrieving weather info
def weather_func(city):
    final_url = weather_url + "q=" + city + "&units=imperial" + "&appid=" + weather_api_key
    req = requests.get(final_url)
    #successful return from OpenWeatherAPI
    if req.status_code == 200:
        res = req.json()
        main_block = res['main']
        temperature = main_block['temp']
        report = res['weather']
        report = report[0]['description']
        for_speech = "The current temperature in " + city + " is " + str(temperature) + " degrees with a report of " + report + "." 
        talk_back(for_speech)
    #could not get weather for given city
    else:
        for_speech = f"Could not retrieve weather for {city}"
        talk_back(for_speech)

#used for all responses from Linda; allows her to talk
def talk_back(string_val,lang_code):
        speech = gtts.gTTS(string_val,lang=lang_code)
        gtts.gTTS(speech)
        print(string_val)
        #generating random file name for temporary speech file
        file_name = str(random.randrange(200)) + "_temp.mp3"
        # saving audio to file
        speech.save(file_name)
        #playing audio file then deleting
        playsound(file_name)
        os.remove(file_name)

# as of now paths are hardcoded, will try to update this later in order to open up; may need to add to PATH environment variable
def open_app(app_name):
    dir = 'shortcuts/' # directory of application shortcuts
    abspath="" # stores path to executable shortcut
    filelist = os.listdir(dir) #obtaining list of files in directory
    file_found = False
    for i in filelist:
        fullfile = os.path.join(dir, i)
        # app was found in shortcuts directory, break for loop and launch it
        if app_name in fullfile.lower():
            abspath = os.path.abspath(fullfile)
            file_found = True
            break
    #application was not found, return to main
    if file_found == False:
        speech_text = f"{app_name} was not found."
        talk_back(speech_text,default_lang)
        return

    speech_text = f"Now opening {app_name}"
    talk_back(speech_text,default_lang)
    os.startfile(abspath) #launching application

#used to queue a song on spotify
def play_song(song_name):
    try:
        if "spotify.exe" not in (i.name().lower() for i in psutil.process_iter()):
            open_app("spotify")
        final_query = ""
        #parsing out the song name
        for val in song_name:
            final_query += val + " "
        final_query = final_query[:-1]
        speech_text = f"now queueing {final_query} on spotify."
        talk_back(speech_text, default_lang)
        #retrieving the data from spotify API based on song search
        track_retrieved = sp.search(q=final_query, limit=1, market="US")
        track = ""
        #parsing out song URI from Spotify API return
        for item in track_retrieved['tracks']['items']:
            track = item['id']
        val = sp.devices()
        #used to check if spotify is currently playing
        playback = sp.current_playback()
        check_active = False
        check_playback = playback['is_playing']
        # if there are no active devices listed, defaults to desktop. Otherwise it plays on the active device.
        if val['devices'] == []:
            sp.add_to_queue(uri=track,device_id='insert_here')
            sp.start_playback(device_id ='insert_here')
        else:
            values = val['devices']
            # double checking for active devices in device dictionary. 
            # if there is an active one, it defaults to that, otherwise it defaults to desktop.
            for devs in values:
                if devs['is_active'] == True:
                    check_active = True
            #an active device was found
            if check_active == True:
                sp.add_to_queue(uri=track,device_id=None)
                if check_playback == False:
                    sp.start_playback(device_id = None)
            #no active device, default to desktop
            else:
                sp.add_to_queue(uri=track,device_id='insert_here')
                if check_playback == False:
                    sp.start_playback(device_id = 'insert_here')
    #song could not be queued
    except:
        speech_text = f"could not queue {song_name}."
        talk_back(speech_text, default_lang)

#used to queue an entire album on spotify
def play_album(song_name):
    try:
        songs_array = []
        if "spotify.exe" not in (i.name().lower() for i in psutil.process_iter()):
            open_app("spotify")
        final_query = ""
        for val in song_name:
            final_query += val + " "
        final_query = final_query[:-1]
        speech_text = f"now queueing the album {final_query} on spotify."
        talk_back(speech_text, default_lang)
        # searching for album on spotify api
        track_retrieved = sp.search(q=final_query, type="album", limit=1, market="US")
        track = ""
        # getting album ID
        for item in track_retrieved['albums']['items']:
            track = item['id']
        # grabbing songs from the given album
        album_songs = sp.album_tracks(album_id=track, market="US")
        # appending all song IDs  from album to be added to queue later
        for item in album_songs['items']:
            track = item['id']
            songs_array.append(track)
        val = sp.devices()
        #used to check current playback to prevent errors
        playback = sp.current_playback()
        check_active = False
        check_playback = playback['is_playing']
        # if there are no active devices listed, defaults to desktop. Otherwise it plays on the active device.
        if val['devices'] == []:
            for song in songs_array:
                sp.add_to_queue(uri=song,device_id='insert_here')
            sp.start_playback(device_id ='insert_here')
        else:
            values = val['devices']
            # double checking for active devices in device dictionary. if there is an active one, it defaults to that, otherwise it defaults to desktop.
            for devs in values:
                if devs['is_active'] == True:
                    check_active = True
            #there is an active device
            if check_active == True:
                for song in songs_array:
                    sp.add_to_queue(uri=song,device_id=None)
                if check_playback == False:
                    sp.start_playback(device_id = None)
            #no active device, default to desktop
            else:
                for song in songs_array:
                    sp.add_to_queue(uri=song,device_id='insert_here')
                if check_playback == False:
                    sp.start_playback(device_id = 'insert_here')
    #album could not be queued
    except:
        speech_text = f"could not queue {song_name}."
        talk_back(speech_text, default_lang)

def pause_playback():
    if "spotify.exe" not in (i.name().lower() for i in psutil.process_iter()):
        open_app("spotify")
    speech_text = ""
    playback = sp.current_playback()
    if playback== None:
        speech_text = "There is currently no playback."
        talk_back(speech_text,default_lang)
        return
    check_playback = playback['is_playing']
    if check_playback == False:
        speech_text = "The playback is already paused."
        talk_back(speech_text, default_lang)
    else:
        speech_text = "Stopping current playback."
        talk_back(speech_text, default_lang)
        sp.pause_playback(device_id=None)

def start_playback():
    if "spotify.exe" not in (i.name().lower() for i in psutil.process_iter()):
        open_app("spotify")
    speech_text = ""
    playback = sp.current_playback()
    if playback == None:
        speech_text = "Starting up Spotify playback."
        talk_back(speech_text, default_lang)
        check_active = False
        val = sp.devices()
        if val['devices'] == []:
            sp.start_playback(device_id ='insert_here')
        else:
            values = val['devices']
            # double checking for active devices in device dictionary. if there is an active one, it defaults to that, otherwise it defaults to desktop.
            for devs in values:
                if devs['is_active'] == True:
                    check_active = True
            #there is an active device
            if check_active == True:
                sp.start_playback(device_id = None)
            #no active device, default to desktop
            else:
                sp.start_playback(device_id = 'insert_here')
    else:
        check_playback = playback['is_playing']
        print("in it")
        if check_playback == True:
            speech_text = "Spotify is already playing."
            talk_back(speech_text, default_lang)
        else:
            speech_text = "Starting up Spotify playback."
            talk_back(speech_text, default_lang)
            check_active = False
            val = sp.devices()
            if val['devices'] == []:
                sp.start_playback(device_id ='insert_here')
            else:
                values = val['devices']
                # double checking for active devices in device dictionary. if there is an active one, it defaults to that, otherwise it defaults to desktop.
                for devs in values:
                    if devs['is_active'] == True:
                        check_active = True
                #there is an active device
                if check_active == True:
                    sp.start_playback(device_id = None)
                #no active device, default to desktop
                else:
                    sp.start_playback(device_id = 'insert_here')

#change the volume on Spotify
def set_volume(value):
    val = sp.devices()
    check_active = False
    volume_value = int(value)
    #invalid volume value
    if volume_value < 0 or volume_value > 100:
        speech_text = "Invalid volume, be sure to choose a volume value between 0 and 100"
        talk_back(speech_text, default_lang)
        return
    speech_text = f"Setting spotify volume to {value}"
    talk_back(speech_text, default_lang)
    # if there are no active devices listed, defaults to desktop. Otherwise it changes volume on the active device.
    if val['devices'] == []:
        sp.volume(volume_percent=volume_value,device_id = 'insert_here')
    else:
        values = val['devices']
        # double checking for active devices in device dictionary. if there is an active one, it defaults to that, otherwise it defaults to desktop.
        for devs in values:
            if devs['is_active'] == True:
                check_active = True
        if check_active == True:
            sp.volume(volume_percent=volume_value,device_id = None)
        else:
            sp.volume(volume_percent=volume_value,device_id = 'insert_here')

def skip_song():
    try:
        speech_text = "Skipping current song."
        talk_back(speech_text, default_lang)
        val = sp.devices()
        #there is no valid device so song cannot be skipped
        if val['devices'] == []:
            print("there is currently no music playing")
        else:
            values = val['devices']
            # double checking for active devices in device dictionary. if there is an active one, it defaults to that, otherwise it defaults to desktop.
            for devs in values:
                if devs['is_active'] == True:
                    check_active = True
            if check_active == True:
                sp.next_track(device_id=None)
            else:
                print("there is currently no music playing")
    #if skipping song fails, notify user
    except:
        speech_text = "Could not skip song."
        talk_back(speech_text, default_lang)

#function used to retrieve sports info
def get_team_info(sports_team, sport):
    #checking each sport to verify it is an accepted sport, then ensuring that a valid team was given for that sport
    if sport == "football":
        try:
            get_record = sports.get_team(sports.FOOTBALL, sports_team)
            scores = get_record.record.split("-")
            speech_text = f"The {str(get_record.name)} have an overall record of {scores[0]} wins, {scores[1]} losses, and {scores[2]} ties."
        except:
            speech_text = f"{sports_team} is an invalid team."
        talk_back(speech_text, default_lang)
    elif sport == "basketball":
        try:
            get_record = sports.get_team(sports.BASKETBALL, sports_team)
            scores = get_record.record.split("-")
            speech_text = f"The {str(get_record.name)} have an overall record of {scores[0]} wins and {scores[1]} losses."
        except:
            speech_text = f"{sports_team} is an invalid team."
        talk_back(speech_text, default_lang)
    elif sport == "baseball":
        try:
            get_record = sports.get_team(sports.BASEBALL, sports_team)
            scores = get_record.record.split("-")
            speech_text = f"The {str(get_record.name)} have an overall record of {scores[0]} wins and {scores[1]} losses."
        except:
            speech_text = f"{sports_team} is an invalid team."
        talk_back(speech_text, default_lang)
    elif sport == "hockey":
        try:
            get_record = sports.get_team(sports.HOCKEY, sports_team)
            scores = get_record.record.split("-")
            speech_text = f"The {str(get_record.name)} have an overall record of {scores[0]} wins, {scores[1]} losses, and {scores[2]} ties."
        except:
            speech_text = f"The {sports_team} is an invalid team."
        talk_back(speech_text, default_lang)
    else:
        speech_text = f"{sport} is an invalid sport, please only use hockey, baseball, basketball, or football."
        talk_back(speech_text, default_lang)

def english_to_foreign(new_language):
    cap_language = str(new_language)
    cap_language = cap_language.capitalize()
    lang_code = ""
    language_found = False
    for key, value in languages.items():
        if value == cap_language:
            lang_code = key
            language_found = True
            break
    if language_found == False:
        speech_text = f"{new_language} is an invalid language."
        talk_back(speech_text, default_lang)
        return
    speech_text = f"Say what you would like to be translated to {new_language}."
    talk_back(speech_text, default_lang)
    wait_phrase = True
    while wait_phrase == True:
        with speech_recognition.Microphone() as mic:
            try:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                # translator = Translator(to_lang=lang_code)
                # translated_string = translator.translate(text)
                translator = Translator()
                translated_string = translator.translate(text,dest=lang_code,src=default_lang).text
                talk_back(translated_string,lang_code)
                if text != "":
                    wait_phrase = False
            except:
                continue

def foreign_to_english(origin_language,new_language):
    print(origin_language)
    print(new_language)
    cap_language = str(origin_language)
    cap_language = cap_language.capitalize()
    lang_code = ""
    language_found = False
    print("definitely here")
    for key, value in languages.items():
        if value == cap_language:
            lang_code = key
            language_found = True
            break
    print("here")
    if language_found == False:
        speech_text = f"{origin_language} is an invalid language."
        talk_back(speech_text, default_lang)
        return
    speech_text = f"Say what you would like to be translated to {new_language}."
    talk_back(speech_text, default_lang)
    wait_phrase = True
    while wait_phrase == True:
        with speech_recognition.Microphone() as mic:
            try:    
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio,language=lang_code)
                text = text.lower()
                translator = Translator()
                translated_string = translator.translate(text,dest=default_lang,src=lang_code).text
                talk_back(translated_string,default_lang)
                if text != "":
                    wait_phrase = False
            except:
                continue

#performs google searches and opens browser
def perform_search(query):
    speech_text = f"Looking up {query}"
    talk_back(speech_text,default_lang)
    webbrowser.open(f"https://google.com/search?q={query}")

#function used to store Linda's possible commands
def commands_list():
    speech_text = random.choice(listening_responses)
    talk_back(speech_text, default_lang)
    with speech_recognition.Microphone() as mic:
        sub_command_bool = True
        while(sub_command_bool == True):
            #recognizing when starting to talk and stopping
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            if "get weather for" in text:
                string_parse = text.split()
                #extracting city name
                city = string_parse[-1]
                #getting weather information from openweathermap api
                weather_func(city)
                sub_command_bool = False
            #used to open up applications
            elif "open up" in text:
                string_parse = text.split()
                application = string_parse[-1]
                open_app(application)
                sub_command_bool = False
            #used to queue songs or albums on spotify
            elif ("queue" or "play") and "on spotify" in text:
                #queueing an album
                if "the album" in text:
                    newtext = text.split()
                    newtexter = newtext[3:-2] #extracted song name
                    play_album(newtexter)
                 #queueing a song
                else:
                    newtext = text.split()
                    newtexter = newtext[1:-2] #extracted song name
                    play_song(newtexter)
                sub_command_bool = False
            #skipping the current song on spotify
            elif "skip song" in text:
                skip_song()
                sub_command_bool = False
            #adjusting the spotify volume
            elif "change spotify volume to" in text:
                newtext = text.split()
                volume_val = newtext[-1]
                set_volume(volume_val)
                sub_command_bool = False
            elif "pause playback" in text:
                print("here")
                pause_playback()
                sub_command_bool = False
            elif "start playback" in text:
                print("here 2")
                start_playback()
                sub_command_bool = False
            #gets information for sports teams
            elif "get team info for" in text:
                newtext = text.split()
                sports_team = ""
                sport = ""
                for strings in newtext[5:-2]:
                    sports_team += strings + " "
                sports_team = sports_team[:-1]
                sport = newtext[-2]
                print(sports_team)
                print(sport)
                get_team_info(sports_team,sport)
                sub_command_bool = False
            #used to translate to foreign languages or foreign languages to english
            elif "translate " and "to" in text:
                newtext = text.split()
                origin_language = newtext[1]
                new_language = newtext[-1]
                if origin_language == "english":
                    english_to_foreign(new_language)
                else:
                    foreign_to_english(origin_language, new_language)
                sub_command_bool = False
            #used to perform google searches
            elif "look up" in text:
                newtext = text.split()
                newtext = newtext[2:]
                query="" 
                for strings in newtext: #filtering query from activation phrase
                    query += strings + " "
                perform_search(query)
                sub_command_bool = False
            #used to exit the command prompt
            elif "nevermind" in text:
                speech_string = "Okay, no problem."
                talk_back(speech_string, default_lang)
                sub_command_bool = False
            #an invalid command was given
            else:
                speech_string = random.choice(invalid_responses)
                talk_back(speech_string, default_lang)

#used to activate Linda via keystroke
def core_function_key():
    while True:
                try:
                    #initiate command list whenever activation key for Linda is pressed
                    if keyboard.is_pressed('f12'):
                        commands_list()
                except:
                    continue
#used to activate Linda via voice activation
def core_function_voice():
    while True:
            with speech_recognition.Microphone() as mic:
                #recognizing when starting to talk and stopping
                try:
                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)
                    text = recognizer.recognize_google(audio)
                    text = text.lower()
                    #used for verifying text at first
                    print(f"Recognized: {text}")
                    #initial command to begin prompt
                    if "hey linda" in text:
                        commands_list()
                except speech_recognition.UnknownValueError:
                    continue

def main():
    #creating processes for both voice activated and key activated Linda
    voice_process = mp.Process(target=core_function_voice)
    text_process = mp.Process(target=core_function_key)
    #starting the processes
    voice_process.start()
    text_process.start()
    #Both processing will continue running until terminate keys are pressed.
    while True:
        if keyboard.is_pressed('del + end'):
            voice_process.terminate()
            text_process.terminate()
            break
    #joining both processes
    voice_process.join()
    text_process.join()
    


if __name__ == "__main__":
    main()