import config
import speaker
import time
import sys


def main():
    general_options: config.Config = config.Config("general")
    speaker_options: config.Config = config.Config("speaker")

    text_speaker: speaker.Speaker = speaker.SpeakerFactory.create(speaker_options)

    if "-d" in sys.argv:
        print("Available Voices:")
        for index, voice in enumerate(text_speaker.get_voices()):
            print(index, voice)

    interval: float = float(general_options.get(["interval"]))
    text: str = general_options.get(["text"])

    while True:
        text_speaker.say(text)
        time.sleep(interval)


if __name__ == "__main__":
    main()
