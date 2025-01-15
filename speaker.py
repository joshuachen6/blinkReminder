import pyttsx3
import pyttsx3.voice
import typing
import config


class Speaker:
    """Speaker to say things with Text-to-speech"""

    def __init__(self) -> None:
        self.__engine: pyttsx3.Engine = pyttsx3.init()
        self.__voice: int = 0

    def set_voice(self, voice: int) -> None:
        self.__voice = voice
        self.__engine.setProperty("voice", self.get_voices()[voice].id)

    def get_voices(self) -> typing.List[pyttsx3.voice.Voice]:
        return self.__engine.getProperty("voices")

    def get_voice(self) -> int:
        return self.__voice

    def get_voice_data(self) -> str:
        return self.__engine.getProperty("voice")

    def set_rate(self, rate: int) -> None:
        self.__engine.setProperty("rate", rate)

    def get_rate(self) -> int:
        return self.__engine.getProperty("rate")

    def set_volume(self, volume: float) -> None:
        self.__engine.setProperty("volume", volume)

    def get_volume(self) -> float:
        return self.__engine.getProperty("volume")

    def say_async(self, text: str) -> None:
        self.__engine.say(text)

    def say(self, text: str) -> None:
        self.say_async(text)
        self.__engine.runAndWait()


class SpeakerFactory:
    @staticmethod
    def create(options: config.Config) -> Speaker:
        speaker: Speaker = Speaker()

        voice: typing.Optional[str] = options.get(["voice"])
        if voice is not None:
            speaker.set_voice(int(voice))

        rate: typing.Optional[str] = options.get(["rate"])
        if rate is not None:
            speaker.set_rate(int(rate))

        volume: typing.Optional[str] = options.get(["volume"])
        if volume is not None:
            speaker.set_volume(float(volume))

        return speaker
