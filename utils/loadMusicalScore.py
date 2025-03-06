from mido import MidiFile, merge_tracks
from typing import List, Tuple


class TextParser:
    KEY = ["QWERTYU", "ASDFGHJ", "ZXCVBNM", "()[]", " "]
    TEMP = ""

    @classmethod
    def parse(cls, filePath: str, bpm: int = 120) -> List[Tuple[float, tuple]]:
        streamNotation = cls.getNotation(filePath)
        events = cls.adjustTime(streamNotation, bpm)
        return events

    @classmethod
    def getNotation(cls, path) -> List:
        notation = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == "":
                    continue
                else:
                    line = line.strip().upper()
                    inParentheses = False
                    inBrackets = False
                    for note in line:
                        if not any(note in char for char in cls.KEY):
                            continue
                        else:
                            if note == "[":
                                inBrackets = True
                                TEMP = "["
                            elif note == "]":
                                inBrackets = False
                                TEMP += "]"
                                notation.append(TEMP)
                            elif inBrackets:
                                TEMP += note
                            elif note == "(":
                                inParentheses = True
                                TEMP = "("
                            elif note == ")":
                                inParentheses = False
                                TEMP += ")"
                                notation.append(TEMP)
                            elif inParentheses:
                                TEMP += note
                            else:
                                notation.append(note)
        return notation

    @classmethod
    def adjustTime(cls, notation, bpm) -> List[Tuple[float, tuple]]:
        currentTime = 0.0
        duration = 60.0 / bpm
        events = []
        for note in notation:
            if len(note) == 1:
                if note == " ":
                    currentTime += duration
                else:
                    events.append((currentTime, tuple(note)))
                    currentTime += duration
            else:
                if note[0] == "[" and note[-1] == "]":
                    if any("(" in char for char in note[1:-1]):
                        TEMPnotes = []
                        inParentheses = False
                        for notes in note[1:-1]:
                            if notes == "(":
                                inParentheses = True
                                TEMP = ""
                            elif notes == ")":
                                inParentheses = False
                                TEMPnotes.append(TEMP)
                            elif inParentheses:
                                TEMP += notes
                            else:
                                TEMPnotes.append(notes)
                        TEMP = duration / len(TEMPnotes)
                        for notes in TEMPnotes:
                            if notes == " ":
                                currentTime += TEMP
                            else:
                                events.append((currentTime, tuple(notes)))
                                currentTime += TEMP
                    else:
                        TEMP = duration / len(note[1:-1])
                        for notes in note[1:-1]:
                            if notes == " ":
                                currentTime += TEMP
                            else:
                                events.append((currentTime, tuple(notes)))
                                currentTime += TEMP
                    currentTime = round(currentTime, 3)
                else:
                    events.append((currentTime, tuple(note[1:-1])))
                    currentTime += duration
        return events


class MidiParser:
    @classmethod
    def parse(cls, filePath: str, bpm: int = 120) -> List[Tuple[float, tuple]]:
        midiFile = MidiFile(filePath)
        track = merge_tracks(midiFile.tracks)

        TYPE = midiFile.type
        TPB = midiFile.ticks_per_beat
        for msg in track:
            if msg.type == "set_tempo":
                TEMPO = msg.tempo
                break

        events = []
        currentTime = 0.0

        for msg in track:
            duration = msg.dict()["time"] / TPB / bpm * 120
            currentTime += duration

            if msg.dict()["type"] == "note_on" and msg.dict()["velocity"] > 0:
                note = cls.getNote(msg.dict()["note"])
                if note is None:
                    continue
                event = [currentTime, tuple(note)]
                events.append(tuple(event))

        events = sorted(events, key=lambda x: x[0])
        events = cls.mergeTuples(events)
        return events

    @staticmethod
    def getNote(value):
        KEY = {
            "QWERTYU": [72, 74, 76, 77, 79, 81, 83],
            "ASDFGHJ": [60, 62, 64, 65, 67, 69, 71],
            "ZXCVBNM": [48, 50, 52, 53, 55, 57, 59],
        }
        for key, values in KEY.items():
            if value in values:
                return key[values.index(value)]
        return None
        # return MidiParser.getNote(value + 1)

    @staticmethod
    def mergeTuples(lst: List) -> List[Tuple[float, tuple]]:
        merged = {}
        for item in lst:
            key = item[0]
            elements = item[1]
            if key in merged:
                merged[key].extend(elements)
            else:
                merged[key] = list(elements)
        # 保持原顺序
        return [(key, tuple(values)) for key, values in merged.items()]


class GmidParser:
    @classmethod
    def parse(cls, filePath: str) -> List[Tuple[float, tuple]]:
        return []


def loadScore(path: str, bpm=120):
    if path.endswith(".txt"):
        Events = TextParser.parse(path, bpm)
    elif path.endswith(".mid"):
        Events = MidiParser.parse(path, bpm)
    elif path.endswith(".gmid"):
        Events = GmidParser.parse(path)
    else:
        print("Unsupported file type")
        return []
    return Events


if __name__ == "__main__":
    # filename = "./Gmidi/songs/欢乐颂.txt"
    # testscore = loadScore(filename, 120)
    # print(testscore)
    filename = "./Gmidi/songs/midi.mid"
    testscore = loadScore(filename, 120)
    print(testscore)
