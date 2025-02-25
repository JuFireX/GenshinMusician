import mido
from mido import MidiFile
from typing import List, Tuple


class GmidParser:
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
    NOTE_NAMES = ["C", "D", "E", "F", "G", "A", "B"]
    OCTAVE_RANGES = {
        "high": (72, 84),  # QWERTYU (C5-C6)
        "mid": (60, 72),  # ASDFGHJ (C4-C5)
        "low": (48, 60),  # ZXCVBNM (C3-C4)
    }

    @classmethod
    def parse(cls, filePath: str, bpm: int = 120) -> List[Tuple[float, tuple]]:
        mid = MidiFile(filePath)
        events = []
        tempo = 500000  # 默认120bpm (500000 μs/beat)
        currentTime = 0.0
        activeNotes = {}  # {note: (start_time, velocity)}

        for track in mid.tracks:
            trackTime = 0.0
            for msg in track:
                trackTime += mido.tick2second(msg.time, mid.ticks_per_beat, tempo)

                if msg.type == "set_tempo":
                    tempo = msg.tempo
                elif msg.type == "note_on" and msg.velocity > 0:
                    activeNotes[msg.note] = (trackTime, msg.velocity)
                elif msg.type in ["note_off", "note_on"] and msg.note in activeNotes:
                    startTime, velocity = activeNotes.pop(msg.note)
                    duration = trackTime - startTime
                    if key := cls._convertMidiNote(msg.note):
                        # 改动
                        if len(events) == 0:
                            events.append((round(startTime, 3), (key,)))
                        elif (round(startTime, 3), (key,)) != events[-1]:
                            events.append((round(startTime, 3), (key,)))

        # 合并多音轨事件并排序
        merged = sorted(events, key=lambda x: x[0])
        return merged

    @classmethod
    def _convertMidiNote(cls, midiNote: int) -> str:
        if midiNote % 12 in [1, 3, 6, 8, 10]:  # 排除半音
            return None

        noteName = cls.NOTE_NAMES[(midiNote - 60) % 12 // 2]
        octave = (midiNote // 12) - 1

        for rangeType, (low, high) in cls.OCTAVE_RANGES.items():
            if low <= midiNote < high:
                offset = (midiNote - low) // 12
                if rangeType == "high":
                    return chr(ord("Q") + offset)
                elif rangeType == "mid":
                    return chr(ord("A") + offset)
                elif rangeType == "low":
                    return chr(ord("Z") + offset)
        return None


def loadScore(path: str, bpm=120):
    if path.endswith(".gmid"):
        Events = GmidParser.parse(path, bpm)
    elif path.endswith(".mid"):
        Events = MidiParser.parse(path)
    else:
        print("Unsupported file type")
        return []
    return Events


if __name__ == "__main__":
    filename = "F:/Code Projects/_Local Projects/GenshinMusician/testplace/0test.gmid"
    testscore = []

    try:
        testscore = loadScore(filename)
        print(f"乐谱文件 '{filename}' 加载成功")
    except FileNotFoundError:
        print(f"乐谱文件 '{filename}' 路径错误")
    except Exception as e:
        print(f"乐谱文件 '{filename}' 加载失败: {e}")

    print(testscore)
