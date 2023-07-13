import pandas as pd


if pd.__version__ != "2.0.3":
    raise Exception("Wrong pandas version ❌")

if __name__ == "__main__":
    print("Project Ran Successfully ✅")