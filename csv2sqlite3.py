from typing import Optional, List
from pathlib import Path
import csv
import sqlite3
import typer
from colorama import init, Fore
from time import time


init(autoreset=True)
app = typer.Typer(add_completion=False)
make_join = lambda lst: ','.join(["'{}'".format(str(i).replace("'", '')) for i in lst])

def check_files(filenames: list, ex: str):
    if not_csv := list(filter(lambda filename: not filename.endswith(f'.{ex}'), [path.name for path in filenames])):
        typer.echo(f"{Fore.RED}E:{Fore.RESET} Invalid filename, '{', '.join(not_csv)}' must be .csv file")
        exit()
    else:
        pass

def get_csv_as_dict(filename: Path) -> dict:
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in list(csv_reader):
            yield row

def get_csv_columns(filename: Path) -> list:
    keys = list([str(key).strip() for key in [dct for dct in get_csv_as_dict(filename)][0].keys()])
    return keys

def db_from_csv(filename: Path, cursor: sqlite3.Cursor) -> None:
    table = filename.name.strip('.csv')
    columns = get_csv_columns(filename)
    sql_command = f"CREATE TABLE IF NOT EXISTS '{table}' ({make_join(columns)})"
    cursor.execute(sql_command)
    typer.echo(f"{Fore.YELLOW}N:{Fore.RESET} Table name: {table}")
    typer.echo(f"{Fore.YELLOW}N:{Fore.RESET} Columns: {columns}")
    counter = 0
    start = time()
    for row in get_csv_as_dict(filename):
        counter += 1
        rows = list(row.values())
        while len(rows) > len(columns):
            rows.pop()
        sql_command = f"INSERT INTO '{table}' VALUES ({make_join(rows)})"
        cursor.execute(sql_command)
    typer.echo(f"{Fore.GREEN}N:{Fore.RESET} Done insert into {table} {counter} rows in {time()-start:.2f}s")

@app.command()
def main(csv_filenames: List[Path], output_filename: Optional[str]="output.sqlite3"):
    check_files(filenames=csv_filenames, ex='csv')
    output_filename = output_filename if output_filename.endswith(('.sqlite3', 'db')) else output_filename+'.sqlite3'
    typer.echo(f"{Fore.YELLOW}N:{Fore.RESET} Output file is {output_filename}")
    con = sqlite3.connect(output_filename)
    cur = con.cursor()
    typer.echo(f"{Fore.YELLOW}N:{Fore.RESET} Done connect with {output_filename}")
    for filename in csv_filenames:
        typer.echo(f"{Fore.YELLOW}N:{Fore.RESET} Working with {filename.name}")
        db_from_csv(filename=filename, cursor=cur)
    con.commit()

if __name__ == "__main__":
    app() 