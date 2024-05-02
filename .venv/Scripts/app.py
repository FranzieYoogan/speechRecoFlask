
from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def index():

    if request.method == 'POST':
  
        r = sr.Recognizer()
        with sr.Microphone() as source:                # use the default microphone as the audio source
         audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

        try:
         data = ("You said: " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
         return render_template('index.htm',data = data)
        except LookupError:                            # speech is unintelligible
          data =  ("Could not understand audio")
          return render_template('index.htm',data = data)
        

    return render_template('index.htm')


app.run(debug=True)