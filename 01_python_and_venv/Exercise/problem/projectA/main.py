import pandas as pd


if pd.__version__ != "1.5.3":
    raise Exception("Wrong pandas version ❌")

if __name__ == "__main__":
    print("Project Ran Successfully ✅")