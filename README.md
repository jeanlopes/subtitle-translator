# Subtitle Translator (Offline, GPU Accelerated)

Offline subtitle translator using Meta NLLB-200 and CUDA acceleration.

## Features

- Fully offline translation
- GPU accelerated (CUDA)
- High quality translation
- Supports SRT files
- Generates bilingual SRT and Excel

## Requirements

- Python 3.10+
- NVIDIA GPU with CUDA support

## Installation

Clone repo:

```bash
git clone https://github.com/yourname/subtitle-translator.git
cd subtitle-translator

Create venv:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Usage
python src/main.py input/legenda.srt

Output will be in:
output/

Model

Uses Meta NLLB-200-distilled-600M

Downloaded automatically on first run.

License

MIT