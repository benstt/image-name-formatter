import os
from pathlib import Path

"""
Format the names of the .jpg or .jpeg files, deleting unnecesary letters.
Example: 
    - IMG-20211014-WA1234.jpg -> 2021-10-14
"""
def format_names(filepath: str) -> None:
    directory = Path(filepath)

    # check if directory is empty
    if len(os.listdir(filepath)) == 0:
        return

    # recursively rename files
    for f in directory.iterdir():
        if f.is_dir():
            format_names(f)
        elif f.is_file():
            if str(f).endswith(".jpg") or str(f).endswith(".jpeg"):
                ppath = str(Path(f).parent.resolve()) # parent path
                fpath = str(Path(f).resolve()) # filepath

                # format new name
                new_name = delete_letters(f.name)
                new_name = add_hyphens(new_name)
                new_path = ppath + "\\" + new_name

                if new_name not in os.listdir(ppath):
                    print(f"Renaming {fpath} to {new_path}...")
                    os.rename(fpath, new_path)

"""
Deletes the letters of the beginning and ending of the name.
"""
def delete_letters(file: str) -> str:
    start: int = file.find("IMG-")
    end: int = file.find("-WA")
    if start == -1 or end == -1:
        return file

    ext = os.path.splitext(file)

    new_name = file[start+4:end] + ext[1]

    return new_name

"""
Add hyphens (-) between the year, month and day.
"""
def add_hyphens(date: str) -> str:
    # check if the date is already formated -- we do not want to add extra hyphens
    is_formatted = date[4] == "-" and date[7] == "-"
    if is_formatted:
        return date

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    return year + "-" + month + "-" + day

format_names(os.getcwd())