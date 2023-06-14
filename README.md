Projekt na przedmiot Teoria kompilacji i kompilatory. Jest to konwerter z asm do c++. 
Napisany w pythonie, przy użyciu ANTLR4 - oparty na visitor.
Gramatyka przyjmowanego formatu wraz ze spisem tokenów znajduje się w pliku MyGrammar.g4
Sposób użycia:
1Przygotuj napisz kod w formacie x86 .asm, zapisz go w pliku np."example.asm"
2Przenies plik do folderu w którym znajduje się plik main.py
3Uruchom plik main.py z dodatkowymi argumentami [1]Nazwa pliku wejsciowego, [2]Nazwa pliku wyjsciowego np. python main.py example.asm example_output.cpp
