import shutil
from argparse import ArgumentParser
from pathlib import Path


def recursive_walk(path: Path, files: list[Path] = None) -> list[Path]:
    files = files or []
    for x in path.iterdir():
        if x.is_file():
            files.append(x.absolute())
            continue
        recursive_walk(x, files)
    return files


def move_files_to_dist(files: list[Path], dest_path: Path) -> None:
    for x in files:
        filename = x.name
        dest_abs_path = (dest_path / x.suffix.replace(".", "")).absolute()
        if not dest_abs_path.exists():
            dest_abs_path.mkdir(parents=True)
        dest_abs_file = dest_abs_path / filename
        shutil.copy(x, dest_abs_file)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--destination", default=Path("dist"), required=False)
    args = parser.parse_args()
    source = Path(args.source)
    if not source.exists():
        exit(f"Source '{args.source}' doesn't exists")
    source_abs = source.absolute()
    dest_abs = Path(args.destination)
    move_files_to_dist(recursive_walk(source_abs), dest_abs)


if __name__ == "__main__":
    main()
