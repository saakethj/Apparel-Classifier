# Merging the csv files of fashion categories
import os
import glob
import pandas as pd

os.chdir("E:/dummy/CSV files/")

extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]


combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv("E:/dummy/combined 1.csv", index=False, encoding="utf-8-sig")
