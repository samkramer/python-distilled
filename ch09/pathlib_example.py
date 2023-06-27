# 9.15.15 pathlib Module
from pathlib import Path

def compute_usage(filename):
    pathname = Path(filename)
    if pathname.is_file():
        return pathname.stat().st_size
    elif pathname.is_dir():
        return sum(path.stat().st_size
                   for path in pathname.rglob('*')
                   if path.is_file())
    else:
        raise RuntimeError('Unsupported file kind')

if __name__ == "__main__":
    filename = Path("/temp/book_code/python/effectivepython/conver.jpg")
    # filename = Path('data/countries.csv')
    print(f"name: {filename.name}")    # 'countries.csv'
    print(f"parent: {filename.parent}")  # 'data'
    print(f"parts: {filename.parts}")   # ('data', 'countries.csv')
    print()
    
    # File
    filepath = "data/countries.csv"
    nbytes = compute_usage(filepath)
    print(f"{filepath}: {nbytes} bytes")
    
    # Directory
    filedir = "data"
    nbytes = compute_usage(filedir)
    print(f"{filedir}: {nbytes} bytes")
