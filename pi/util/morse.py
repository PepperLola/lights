pauses = {
    "-": 3,
    ".": 1,
    " ": 3,
    "/": 7
}

INTER_MORSE_CHAR_PAUSE = 1

chars = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def to_morse(text: str) -> str:
    words = text.lower().split(" ")
    words = map(lambda word: " ".join(list(map(lambda c: chars[c] if c in chars.keys() else "", list(word)))), words)
    return "/".join(words) + " " # add space to end to automatically pause between repeats

def get_pauses(morse: str) -> list[tuple[bool, int]]:
    ret = []
    for i in range(len(morse)):
        c = morse[i]
        if c in ".-":
            ret.append((True, pauses[c]))
            # don't do inter-character pause if not between characters in word
            if i < len(morse) - 1 and morse[i+1] != " ":
                ret.append((False, INTER_MORSE_CHAR_PAUSE)) # pause between .-
        elif c in pauses.keys():
            ret.append((False, pauses[c]))
    return ret
