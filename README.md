# 🩻cxr-ios

## steps

1. Download data from: [nihcc](https://nihcc.app.box.com/v/ChestXray-NIHCC) or [kaggle](https://www.kaggle.com/datasets/nih-chest-xrays/data?resource=download)
2. All images from sub directory of images are copied into `all_images/` folder with `copy_images.py`.
3. change csv file name from `Data_Entry_2017_v2020.csv` to `data.csv`
4. make a simpler `data2.csv` with `simplify_csv.py`: remove columns, rename columns, ignore "No Finding" in "Finding Labels"

   ```csv
   <!-- original columns -->
   Image Index,Finding Labels,Follow-up #,Patient ID,Patient Age,Patient Gender,View Position,OriginalImage[Width,Height],OriginalImagePixelSpacing[x,y],

   <!-- columns removed -->
   Image Index,Finding Labels,Patient Age,Patient Gender,View Position

   <!-- renamed -->
   name,label,age,gender,position

   <!-- image names changed from png to jpg -->
   ```

5. make `db.sqlite3` form `data2.csv` with `csv_to_sqlite.py`
6. 1024x1024 png images from `all_images/` that exists in `data2.csv` ignoring the extension of the image files are resized to 512x512 jpg images with `resize_images.py` into `resized_images/`.

   > ⚠︎ this takes very long time e.g. 783s
