# He agafat el teu exemple de mapper i l'he modificat amb la informació del link: 
# https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l
import re
import sys
import io
import re
import nltk
import string
from unicodedata import normalize
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
# Posam els signes de puntuació que existeixen a l'alfabet llatí
puntuacions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Agafam les stopwords per eliminar-les dels llenguatges que hem triat. En el meu cas, els llibres que he elegit estan escrits en italià, portuguès i espanyol.
stop_words = stopwords.words('italian') + stopwords.words('spanish') + stopwords.words('portuguese')
stop_words = set(stop_words)
# Feim que l'encoding utilitzat per llegir les línees dels arxius sigui latin1.
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')

# Llegim les línees dels llibres i eliminam les senyals de puntuació.
for line in input_stream:
  line = line.strip()
  # Llevam els digits amb \w i els espais en blanc amb \s.
  line = re.sub(r'[^\w\s]', '',line)
  # Feim lower per no distingir entre majúscules i minúscules.
  line = line.lower()
  for x in line:
    if x in puntuacions:
      line=line.replace(x, " ") 

  words=line.split()
  for word in words: 
    if word not in stop_words:
        # Si les paraules dels arxius no són stopwords els hi llevarem l'accent amb la comanda trobada al link:
        # https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l
        # Així feim que totes les paraules tenguin lletres comuns de l'alfabet llatí.
        word = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                normalize( "NFD", word), 0, re.I
            )

        # -> NFC
        word = normalize( 'NFC', word)
        # Agafam la primera lletra de les paraules.
        lletra = word[0:1]
        # Si la lletra esta a la llista de lletres de l'alfabet llatí, la mostrarà per pantalla, amb 
        if lletra in list('abcdefghijklmnñopqrstuvwxyzç'):
          print('%s\t%s' % (lletra, 1))
