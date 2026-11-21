"""Copy the declared fitting artifacts into the steering workflow's run tree."""

from pathlib import Path
from shutil import copyfile
from typing import Mapping


def main(inputs: Mapping[str, Path], outputs: Mapping[str, Path]) -> None:
    for slot, destination in outputs.items():
        copyfile(inputs[slot], destination)
