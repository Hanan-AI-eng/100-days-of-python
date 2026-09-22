from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
NAMES_FILE = PROJECT_DIR / "Input" / "Names" / "invited_names.txt"
TEMPLATE_FILE = PROJECT_DIR / "Input" / "Letters" / "starting_letter.txt"
OUTPUT_DIR = PROJECT_DIR / "Output" / "ReadyToSend"


def generate_letters(
    names_file: Path = NAMES_FILE,
    template_file: Path = TEMPLATE_FILE,
    output_dir: Path = OUTPUT_DIR,
) -> None:
    """Create one letter for each name in the names file."""
    names = names_file.read_text(encoding="utf-8").splitlines()
    template = template_file.read_text(encoding="utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)

    for name in names:
        name = name.strip()
        if not name:
            continue
        letter = template.replace("[name]", name)
        (output_dir / f"message_for_{name}.docx").write_text(
            letter,
            encoding="utf-8",
        )


if __name__ == "__main__":
    generate_letters()
