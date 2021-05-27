# Data Transform .mdb to .csv

### 先使用mdbtools將mdb轉為csv
1. 安裝mdbtools
```bash=
sudo apt-get install mdbtools
```
2. clone mdbtools 轉檔的sh
```bash=
git clone https://github.com/pavlov99/mdb-export-all.git
```
3. 轉檔後輸出至`mdb-export-all/{mdb file name}/查詢.csv`
```bash=
cd mdb-export-all
bash mdb-export-all.sh {mdb file path}
cp {mdb file name}/查詢.csv home/ubuntu/data_transform/data/data.csv
```

### 將mdbtools輸出的csv做data_transform
```bash=
cp {mdb file name}/查詢.csv home/ubuntu/data_transform/data/data.csv
cd home/ubuntu/data_transform
python3 data_transform.py
```