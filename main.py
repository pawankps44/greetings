from greets import Greetings
from translate import Translator

translator = Translator('pt')

for g in Greetings:
    print(translator.translate(g).title())
