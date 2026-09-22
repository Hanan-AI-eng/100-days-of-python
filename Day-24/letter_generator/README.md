# Letter Generator

This Day-24 project practices working with files, directories, and paths. It
reads names from `Input/Names/invited_names.txt`, replaces `[name]` in
`Input/Letters/starting_letter.txt`, and writes one letter per name to
`Output/ReadyToSend`.

Run it from the repository root:

```powershell
python Day-24/letter_generator/main.py
```

You can also run it after changing into this project directory:

```powershell
cd Day-24/letter_generator
python main.py
```

The script reads the names and template from `Input/` and writes one generated
file per name to `Output/ReadyToSend/`. The generated files are intentionally
ignored from version control.
