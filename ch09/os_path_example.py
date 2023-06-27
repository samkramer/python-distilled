# 9.15.14 os.path Module
import os.path

# REF:
# https://note.nkmk.me/en/python-os-path-getsize/

def compute_usage(filename):
    if os.path.isfile(filename):
        return os.path.getsize(filename)
    elif os.path.isdir(filename):
        return sum(compute_usage(os.path.join(filename, name)) 
                   for name in os.listdir(filename))
    else:
        raise RuntimeError('Unsupported file kind')

if __name__ == "__main__":
    # File
    filepath = "data/countries.csv"
    filename = os.path.basename(filepath)
    nbytes = compute_usage(filepath)
    print(f"{filename}: {nbytes} bytes")
    
    # Directory
    filedir = "data"
    nbytes = compute_usage(filedir)
    print(f"{filedir}: {nbytes} bytes")
    
    # Equivalent functionality to calculate total number of bytes
    # in a directory using PowerShell
    # Get-ChildItem | Measure-Object -Property Length -Sum | Select-Object -ExpandProperty Sum
    