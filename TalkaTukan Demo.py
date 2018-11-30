#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat


def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    
    led.set_state(aiy.voicehat.LED.BLINK)

    
    # LOOP SOM VÄNTAR PÅ EN KNAPPTRYCk OCH SEDAN LYSSNAR EFTER EN RöST 
    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        
        # OM KOMMANDOT INTE UPPFATTADES SOM TEXT
        if not text:
            print('Sorry, I did not hear you.')
            
        # OLIKA ALTERNATIV FÖR ATT MATCHA EN KÄND TEXT OCH GÖRA NÅGOT 
        else:
            print('You said "', text, '"') #SKRIV UT TILL SKÄRMEN
            if 'turn on the light' in text:
                led.set_state(aiy.voicehat.LED.ON)
            elif 'turn off the light' in text:
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'blink' in text:
                led.set_state(aiy.voicehat.LED.BLINK)
            
            elif 'repeat after me' in text:
                to_repeat = text.replace('repeat after me', '', 1)
                aiy.audio.say(to_repeat)
                
            elif 'my name is' in text:
                to_repeat = 'hi there ' + text.replace ('my name is', '', 1)
                aiy.audio.say(to_repeat)
            
            elif text == 'what\'s your name':
                to_repeat = 'My name is Talka Toucan. Whats yours? '
                aiy.audio.say(to_repeat)
            
            elif 'goodbye' in text:
                to_repeat = "Goodbye. It was nice talking to you."
                aiy.audio.say(to_repeat)
                break
            elif "how old are you" in text:
                to_repeat = "I am 3 years old, which is quite young for a toucan."
                aiy.audio.say(to_repeat)
            elif "how is the weather" in text:
                to_repeat = "It is always nice weather in Universeums rainforest."
                aiy.audio.say(to_repeat)
            elif "what is your favorite color" in text:
                to_repeat = "My favourite colour is yellow"
                aiy.audio.say(to_repeat)
            elif "nice to meet you" in text:
                to_repeat = "nice to meet you to, are you having a good day"
                aiy.audio.say(to_repeat)
                

if __name__ == '__main__':
    main()
