
### Step 1: Object detection

```
git clone https://github.com/ultralytics/yolov5  # clone repo
pip install -qr requirements.txt # install dependencies
python object_detection.py
cd yolov5
python yolov5/train.py --img 416 --batch 16 --epochs 50 --data ./Passport-4/data.yaml --weights yolov5s.pt --cache
```

### Step 2: Easy OCR
```
python crop.py
python easy_ocr.py
```

### Step 4: NER
```
python ner.py
```
### Step 5: Post-processing
```
python post_processing.py
```