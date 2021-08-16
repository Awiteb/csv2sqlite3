<center><h1>csv2sqlite3</h1></center>
<center><b>csv2sqlite3 It is a command line tool that helps you to add one or more csv tables to a sqlite3 database.</b></center>
<br>
<p align="center">
  <a href="#Requirements">Requirements</a>
  •
  <a href="#Install">Install</a>
  •
  <a href="#Uses">Uses</a>
  •
  <a href="#Example">Example</a>
  <br>
  <a href="#License">License</a>
</p>

## Requirements
* **[python3.8](https://www.python.org/downloads/) +**
* **[git](https://git-scm.com/)**
* **[pip](https://pip.pypa.io/en/stable/installation/)**

## Install
use [GitHub](https://github.com/) to clone the tool
```bash
git clone https://github.com/Awiteb/csv2sqlite3
cd csv2sqlite3
pip3 install -r requirements.txt
```

## Uses
```text
Usage: csv2sqlite3.py [OPTIONS] CSV_FILENAMES...

Arguments:
  CSV_FILENAMES...  [required]

Options:
  --output-filename TEXT  [default: output.sqlite3]
  --help                  Show this message and exit.

```

## Example

```bash
python3 file1.csv file2.csv file3.csv
```
```bash
python3 --output-filename my_db.db file1.csv
```

## License
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)