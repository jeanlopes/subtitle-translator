import pysrt
import pandas as pd
import argparse
from pathlib import Path

from translator import Translator


def run(input_file, output_excel, output_srt=None):

    print("Loading subtitles...")

    subs = pysrt.open(input_file, encoding="utf-8")

    english = [sub.text.replace("\n", " ") for sub in subs]

    translator = Translator()

    print("Translating...")
    portuguese = translator.translate_batch(english)

    print("Saving Excel...")

    df = pd.DataFrame({
        "Index": [sub.index for sub in subs],
        "Timestamp": [
            f"{sub.start} --> {sub.end}"
            for sub in subs
        ],
        "English": english,
        "Portuguese": portuguese
    })

    Path("output").mkdir(exist_ok=True)

    df.to_excel(output_excel, index=False)

    if output_srt:

        print("Saving bilingual SRT...")

        for sub, pt in zip(subs, portuguese):

            sub.text = f"{sub.text}\n{pt}"

        subs.save(output_srt, encoding="utf-8")

    print("Finished.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("input")

    parser.add_argument(
        "--excel",
        default="output/translated.xlsx"
    )

    parser.add_argument(
        "--srt",
        default="output/translated.srt"
    )

    args = parser.parse_args()

    run(
        args.input,
        args.excel,
        args.srt
    )
