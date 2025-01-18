
# Diccionarios para letras griegas
consonants_mapping = {
    'b': 'β', 'c': 'χ', 'd': 'δ', 'f': 'φ', 'g': 'γ', 'j': 'ς', 'k': 'κ',
    'l': 'λ', 'm': 'μ', 'n': 'ν', 'p': 'π', 'q': 'θ', 'r': 'ρ', 's': 'σ',
    't': 'τ', 'v': 'ϝ', 'y': 'ψ', 'x': 'ξ', 'z': 'ζ',
    'B': 'Β', 'C': 'Χ', 'D': 'Δ', 'F': 'Φ', 'G': 'Γ', 'J': 'Σ', 'K': 'Κ',
    'L': 'Λ', 'M': 'Μ', 'N': 'Ν', 'P': 'Π', 'Q': 'Θ', 'R': 'Ρ', 'S': 'Σ',
    'T': 'Τ', 'V': 'Ϝ', 'Y': 'Ψ', 'X': 'Ξ', 'Z': 'Ζ'
}

vowels_mapping = {
    # Minúsculas
    'a': 'α', 'e': 'ε', 'i': 'ι', 'o': 'ο', 'u': 'υ', 'h': 'η', 'w': 'ω',
    # Mayúsculas
    'A': 'Α', 'E': 'Ε', 'I': 'Ι', 'O': 'Ο', 'U': 'Υ', 'H': 'Η', 'W': 'Ω'
}

# Combinaciones posibles
spirits = {'>': '̓', '<': '̔'}  # Espíritu suave y áspero
accents = {"\u00b4": '́', '`': '̀', '^': '͂'}  # Agudo, grave y circunflejo
iota_subscript = {"'": 'ͅ'}  # Iota suscrita

pending_modifiers = []  # Lista para almacenar modificadores pendientes (espíritus, acentos, etc.)
MODIFIER_ORDER = {'spirit': 1, 'accent': 2, 'iota': 3}

# Diccionario de equivalencias precompuestas
precomposed_chars = {
    # Alfa Minúscula
    '\u03b1': 'α',        # Alfa
    '\u03b1\u0313': 'ἀ',  # Alfa con espíritu suave
    '\u03b1\u0314': 'ἁ',  # Alfa con espíritu áspero
    '\u03b1\u0301': 'ά',  # Alfa con acento agudo
    '\u03b1\u0300': 'ὰ',  # Alfa con acento grave
    '\u03b1\u0342': 'ᾶ',  # Alfa con circunflejo
    '\u03b1\u0345': 'ᾳ',  # Alfa con iota suscrita 
    '\u03b1\u0313\u0301': 'ἄ',  # Alfa con espíritu suave y acento agudo
    '\u03b1\u0314\u0301': 'ἅ',  # Alfa con espíritu áspero y acento agudo
    '\u03b1\u0313\u0345': 'ᾀ',  # Alfa con espíritu suave e iota suscrita
    '\u03b1\u0314\u0345': 'ᾁ',  # Alfa con espíritu áspero e iota suscrita
    '\u03b1\u0313\u0301\u0345': 'ᾄ',  # Alfa con espíritu suave, acento agudo e iota suscrita
    '\u03b1\u0314\u0301\u0345': 'ᾅ',  # Alfa con espíritu áspero, acento agudo e iota suscrita
    '\u03b1\u0313\u0300': 'ἂ',  # Alfa con espíritu suave y acento grave
    '\u03b1\u0314\u0300': 'ἃ',  # Alfa con espíritu áspero y acento grave
    '\u03b1\u0313\u0300\u0345': 'ᾂ',  # Alfa con espíritu suave, acento grave e iota suscrita
    '\u03b1\u0314\u0300\u0345': 'ᾃ',  # Alfa con espíritu áspero, acento grave e iota suscrita
    '\u03b1\u0342\u0345': 'ᾷ',  # Alfa con circunflejo e iota suscrita
    '\u03b1\u0314\u0342': 'ἆ',  # Alfa con circunflejo y espíritu áspero
    '\u03b1\u0313\u0342': 'ἇ',  # Alfa con circunflejo y espíritu suave
    '\u03b1\u0314\u0342\u0345': 'ᾇ',  # Alfa con circunflejo, espíritu áspero e iota suscrita
    '\u03b1\u0313\u0342\u0345': 'ᾆ',  # Alfa con circunflejo, espíritu suave e iota suscrita

    # Alfa Mayúscula
    '\u0391': 'Α',  # Alfa mayúscula
    '\u0391\u0313': 'Ἀ',  # Alfa mayúscula con espíritu suave
    '\u0391\u0313\u0301': 'Ἄ',  # Alfa mayúscula con espíritu suave y acento agudo
    '\u0391\u0313\u0300': 'Ἂ',  # Alfa mayúscula con espíritu suave y acento grave
    '\u0391\u0313\u0342': 'Ἆ',  # Alfa mayúscula con espíritu suave y circunflejo
    '\u0391\u0313\u0345': 'ᾈ',  # Alfa mayúscula con espíritu suave e iota suscrita
    '\u0391\u0313\u0342\u0345': 'ᾎ',  # Alfa mayúscula con espíritu suave, circunflejo e iota suscrita
    '\u0391\u0314': 'Ἁ',  # Alfa mayúscula con espíritu áspero
    '\u0391\u0314\u0301': 'Ἅ',  # Alfa mayúscula con espíritu áspero y acento agudo
    '\u0391\u0314\u0300': 'Ἃ',  # Alfa mayúscula con espíritu áspero y acento grave
    '\u0391\u0314\u0342': 'Ἇ',  # Alfa mayúscula con espíritu áspero y circunflejo
    '\u0391\u0314\u0345': 'ᾉ',  # Alfa mayúscula con espíritu áspero e iota suscrita
    '\u0391\u0314\u0342\u0345': 'ᾏ',  # Alfa mayúscula con espíritu áspero, circunflejo e iota suscrita
    '\u0391\u0301': 'Ά',  # Alfa mayúscula con acento agudo
    '\u0391\u0300': 'Ὰ',  # Alfa mayúscula con acento grave
    '\u0391\u0345': 'ᾼ',  # Alfa mayúscula con iota suscrita

    # Épsilon minúscula
    '\u03b5': 'ε',  # Épsilon
    '\u03b5\u0313': 'ἐ',  # Épsilon con espíritu suave
    '\u03b5\u0314': 'ἑ',  # Épsilon con espíritu áspero
    '\u03b5\u0301': 'έ',  # Épsilon con acento agudo
    '\u03b5\u0313\u0301': 'ἔ',  # Épsilon con espíritu suave y acento agudo
    '\u03b5\u0314\u0301': 'ἕ',  # Épsilon con espíritu áspero y acento agudo
    '\u03b5\u0300': 'ὲ',        # Épsilon con acento grave
    '\u03b5\u0313\u0300': 'ἒ',  # Épsilon con acento grave y espíritu suave
    '\u03b5\u0314\u0300': 'ἓ',  # Épsilon con acento grave y espíritu áspero

    # Épsilon mayúscula
    '\u0395': 'Ε',  # Épsilon mayúscula
    '\u0395\u0313': 'Ἐ',  # Épsilon mayúscula con espíritu suave
    '\u0395\u0313\u0301': 'Ἔ',  # Épsilon mayúscula con espíritu suave y acento agudo
    '\u0395\u0313\u0300': 'Ἒ',  # Épsilon mayúscula con espíritu suave y acento grave
    '\u0395\u0314': 'Ἑ',  # Épsilon mayúscula con espíritu áspero
    '\u0395\u0314\u0301': 'Ἕ',  # Épsilon mayúscula con espíritu áspero y acento agudo
    '\u0395\u0314\u0300': 'Ἓ',  # Épsilon mayúscula con espíritu áspero y acento grave
    '\u0395\u0301': 'Έ',  # Épsilon mayúscula con acento agudo
    '\u0395\u0300': 'Ὲ',  # Épsilon mayúscula con acento grave

    # Iota minúscula
    '\u03b9': 'ι',  # Iota
    '\u03b9\u0313': 'ἰ',  # Iota con espíritu suave
    '\u03b9\u0314': 'ἱ',  # Iota con espíritu áspero
    '\u03b9\u0301': 'ί',  # Iota con acento agudo
    '\u03b9\u0313\u0301': 'ἴ',  # Iota con espíritu suave y acento agudo
    '\u03b9\u0314\u0301': 'ἵ',  # Iota con espíritu áspero y acento agudo
    '\u03b9\u0300': 'ὶ',        # Iota con acento grave
    '\u03b9\u0313\u0300': 'ἲ',  # Iota con acento grave y espíritu suave
    '\u03b9\u0314\u0300': 'ἳ',  # Iota con acento grave y espíritu áspero
    '\u03b9\u0342': 'ῖ',        # Iota con circunflejo
    '\u03b9\u0313\u0342': 'ἶ',  # Iota con circunflejo y espíritu suave
    '\u03b9\u0314\u0342': 'ἷ',  # Iota con circunflejo y espíritu áspero

    # Iota mayúscula
    '\u0399': 'Ι',  # Iota
    '\u0399\u0313': 'Ἰ',  # Iota con espíritu suave
    '\u0399\u0313\u0301': 'Ἴ',  # Iota con espíritu suave y acento agudo
    '\u0399\u0313\u0300': 'Ἲ',  # Iota con espíritu suave y acento grave
    '\u0399\u0313\u0342': 'Ἶ',  # Iota con espíritu suave y circunflejo
    '\u0399\u0314': 'Ἱ',  # Iota con espíritu áspero
    '\u0399\u0314\u0301': 'Ἵ',  # Iota con espíritu áspero y acento agudo
    '\u0399\u0314\u0300': 'Ἳ',  # Iota con espíritu áspero y acento grave
    '\u0399\u0314\u0342': 'Ἷ',  # Iota con espíritu áspero y circunflejo
    '\u0399\u0301': 'Ί',  # Iota con acento agudo
    '\u0399\u0300': 'Ὶ',  # Iota con acento grave


    # Ómicron minúscula
    '\u03bf': 'ο',  # Ómicron
    '\u03bf\u0313': 'ὀ',  # Ómicron con espíritu suave
    '\u03bf\u0314': 'ὁ',  # Ómicron con espíritu áspero
    '\u03bf\u0301': 'ό',  # Ómicron con acento agudo
    '\u03bf\u0313\u0301': 'ὄ',  # Ómicron con espíritu suave y acento agudo
    '\u03bf\u0314\u0301': 'ὅ',  # Ómicron con espíritu áspero y acento agudo
    '\u03bf\u0300': 'ὸ',        # Ómicron con acento grave
    '\u03bf\u0313\u0300': 'ὂ',  # Ómicron con acento grave y espíritu suave
    '\u03bf\u0314\u0300': 'ὃ',  # Ómicron con acento grave y espíritu áspero


    # Ómicron mayúscula
    '\u039f': 'Ο',  # Ómicron mayúscula
    '\u039f\u0313': 'Ὀ',  # Ómicron mayúscula con espíritu suave
    '\u039f\u0313\u0301': 'Ὄ',  # Ómicron mayúscula con espíritu suave y acento agudo
    '\u039f\u0313\u0300': 'Ὂ',  # Ómicron mayúscula con espíritu suave y acento grave
    '\u039f\u0314': 'Ὁ',  # Ómicron mayúscula con espíritu áspero
    '\u039f\u0314\u0301': 'Ὅ',  # Ómicron mayúscula con espíritu áspero y acento agudo
    '\u039f\u0314\u0300': 'Ὃ',  # Ómicron mayúscula con espíritu áspero y acento grave
    '\u039f\u0301': 'Ό',  # Ómicron mayúscula con acento agudo
    '\u039f\u0300': 'Ὸ',  # Ómicron mayúscula con acento grave

    # Upsilon minúscula
    '\u03c5': 'υ',  # Upsilon
    '\u03c5\u0313': 'ὐ',  # Upsilon con espíritu suave
    '\u03c5\u0314': 'ὑ',  # Upsilon con espíritu áspero
    '\u03c5\u0301': 'ύ',  # Upsilon con acento agudo
    '\u03c5\u0313\u0301': 'ὔ',  # Upsilon con espíritu suave y acento agudo
    '\u03c5\u0314\u0301': 'ὕ',  # Upsilon con espíritu áspero y acento agudo
    '\u03c5\u0300': 'ὺ',        # Upsilon con acento grave
    '\u03c5\u0313\u0300': 'ὒ',  # Upsilon con acento grave y espíritu suave
    '\u03c5\u0314\u0300': 'ὓ',  # Upsilon con acento grave y espíritu áspero
    '\u03c5\u0342': 'ῦ',        # Upsilon con circunflejo
    '\u03c5\u0313\u0342': 'ὖ',  # Upsilon con circunflejo y espíritu suave
    '\u03c5\u0314\u0342': 'ὗ',  # Upsilon con circunflejo y espíritu áspero

    # Upsilon mayúscula
    '\u03a5': 'Υ',  # Úpsilon
    '\u03a5\u0314\u0301': 'Ὕ',  # Úpsilon con espíritu áspero y acento agudo
    '\u03a5\u0314\u0300': 'Ὓ',  # Úpsilon con espíritu áspero y acento grave
    '\u03a5\u0314\u0342': 'Ὗ',  # Úpsilon con espíritu áspero y circunflejo
    '\u03a5\u0301': 'Ύ',  # Úpsilon con acento agudo
    '\u03a5\u0300': 'Ὺ',  # Úpsilon con acento grave

    
    # Eta minúscula
    '\u03b7': 'η',  # Eta
    '\u03b7\u0313': 'ἠ',  # Eta con espíritu suave
    '\u03b7\u0314': 'ἡ',  # Eta con espíritu áspero
    '\u03b7\u0301': 'ή',  # Eta con acento agudo
    '\u03b7\u0345': 'ῃ',  # Eta con iota suscrita
    '\u03b7\u0313\u0301': 'ἤ',  # Eta con espíritu suave y acento agudo
    '\u03b7\u0314\u0301': 'ἥ',  # Eta con espíritu áspero y acento agudo
    '\u03b7\u0313\u0345': 'ᾐ',  # Eta con espíritu suave e iota suscrita
    '\u03b7\u0314\u0345': 'ᾑ',  # Eta con espíritu áspero e iota suscrita
    '\u03b7\u0313\u0301\u0345': 'ᾔ',  # Eta con espíritu suave, acento agudo e iota suscrita
    '\u03b7\u0314\u0301\u0345': 'ᾕ',  # Eta con espíritu áspero, acento agudo e iota suscrita
    '\u03b7\u0300': 'ὴ',            # Eta con acento grave
    '\u03b7\u0313\u0300': 'ἢ',      # Eta con acento grave y espíritu suave
    '\u03b7\u0314\u0300': 'ἣ',      # Eta con acento grave y espíritu áspero
    '\u03b7\u0300\u0345': 'ῂ',      # Eta con acento grave e iota suscrita
    '\u03b7\u0342': 'ῆ',            # Eta con circunflejo
    '\u03b7\u0313\u0342': 'ἦ',      # Eta con circunflejo y espíritu suave
    '\u03b7\u0314\u0342': 'ἧ',      # Eta con circunflejo y espíritu áspero
    '\u03b7\u0342\u0345': 'ῇ',      # Eta con circunflejo e iota suscrita
    '\u03b7\u0313\u0342\u0345': 'ᾖ',  # Eta con circunflejo, espíritu suave e iota suscrita
    '\u03b7\u0314\u0342\u0345': 'ᾗ',  # Eta con circunflejo, espíritu áspero e iota suscrita

    # Eta mayúscula
    '\u0397': 'Η',  # Eta
    '\u0397\u0313': 'Ἠ',  # Eta con espíritu suave
    '\u0397\u0313\u0301': 'Ἤ',  # Eta con espíritu suave y acento agudo
    '\u0397\u0313\u0300': 'Ἢ',  # Eta con espíritu suave y acento grave
    '\u0397\u0313\u0342': 'Ἦ',  # Eta con espíritu suave y circunflejo
    '\u0397\u0313\u0345': 'ᾘ',  # Eta con espíritu suave y iota suscrita
    '\u0397\u0313\u0342\u0345': 'ᾞ',  # Eta con espíritu suave, circunflejo e iota suscrita
    '\u0397\u0314': 'Ἡ',  # Eta con espíritu áspero
    '\u0397\u0314\u0301': 'Ἥ',  # Eta con espíritu áspero y acento agudo
    '\u0397\u0314\u0300': 'Ἣ',  # Eta con espíritu áspero y acento grave
    '\u0397\u0314\u0342': 'Ἧ',  # Eta con espíritu áspero y circunflejo
    '\u0397\u0314\u0345': 'ᾙ',  # Eta con espíritu áspero y iota suscrita
    '\u0397\u0314\u0342\u0345': 'ᾟ',  # Eta con espíritu áspero, circunflejo e iota suscrita
    '\u0397\u0301': 'Ή',  # Eta con acento agudo
    '\u0397\u0300': 'Ὴ',  # Eta con acento grave
    '\u0397\u0345': 'ῌ',  # Eta con iota suscrita

    # Omega minúscula
    '\u03c9': 'ω',  # Omega
    '\u03c9\u0313': 'ὠ',  # Omega con espíritu suave
    '\u03c9\u0314': 'ὡ',  # Omega con espíritu áspero
    '\u03c9\u0301': 'ώ',  # Omega con acento agudo
    '\u03c9\u0345': 'ῳ',  # Omega con iota suscrita
    '\u03c9\u0313\u0301': 'ὤ',  # Omega con espíritu suave y acento agudo
    '\u03c9\u0314\u0301': 'ὥ',  # Omega con espíritu áspero y acento agudo
    '\u03c9\u0300': 'ὼ',        # Omega con acento grave
    '\u03c9\u0313\u0300': 'ὢ',  # Omega con acento grave y espíritu suave
    '\u03c9\u0314\u0300': 'ὣ',  # Omega con acento grave y espíritu áspero
    '\u03c9\u0300\u0345': 'ῲ',  # Omega con acento grave e iota suscrita
    '\u03c9\u0342': 'ῶ',        # Omega con circunflejo
    '\u03c9\u0313\u0342': 'ὦ',  # Omega con circunflejo y espíritu suave
    '\u03c9\u0314\u0342': 'ὧ',  # Omega con circunflejo y espíritu áspero
    '\u03c9\u0342\u0345': 'ῷ',  # Omega con circunflejo e iota suscrita
    '\u03c9\u0313\u0342\u0345': 'ᾦ',  # Omega con circunflejo, espíritu suave e iota suscrita
    '\u03c9\u0314\u0342\u0345': 'ᾧ',  # Omega con circunflejo, espíritu áspero e iota suscrita

    # Omega mayúscula
    '\u03a9': 'Ω',  # Omega
    '\u03a9\u0313': 'Ὠ',  # Omega con espíritu suave
    '\u03a9\u0313\u0301': 'Ὤ',  # Omega con espíritu suave y acento agudo
    '\u03a9\u0313\u0300': 'Ὢ',  # Omega con espíritu suave y acento grave
    '\u03a9\u0313\u0342': 'Ὦ',  # Omega con espíritu suave y circunflejo
    '\u03a9\u0313\u0345': 'ᾨ',  # Omega con espíritu suave y iota suscrita
    '\u03a9\u0313\u0342\u0345': 'ᾮ',  # Omega con espíritu suave, circunflejo e iota suscrita
    '\u03a9\u0314': 'Ὡ',  # Omega con espíritu áspero
    '\u03a9\u0314\u0301': 'Ὥ',  # Omega con espíritu áspero y acento agudo
    '\u03a9\u0314\u0300': 'Ὣ',  # Omega con espíritu áspero y acento grave
    '\u03a9\u0314\u0342': 'Ὧ',  # Omega con espíritu áspero y circunflejo
    '\u03a9\u0314\u0345': 'ᾩ',  # Omega con espíritu áspero y iota suscrita
    '\u03a9\u0314\u0342\u0345': 'ᾯ',  # Omega con espíritu áspero, circunflejo e iota suscrita
    '\u03a9\u0301': 'Ώ',  # Omega con acento agudo
    '\u03a9\u0300': 'Ὼ',  # Omega con acento grave
    '\u03a9\u0345': 'ῼ',  # Omega con iota suscrita
}
