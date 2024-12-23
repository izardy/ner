### Create config.cfg file
```
python -m spacy init fill-config ./base_config.cfg ./config.cfg
```
### Train the model
```
python -m spacy train config.cfg --output ./output --paths.train ./train --paths.dev ./dev --gpu-id 0 # if using gpu to train
# python -m spacy train config.cfg --output ./output --paths.train ./train --paths.dev ./dev # if using cpu to train
```

#### Result

```
=========================== Initializing pipeline ===========================
✔ Initialized pipeline

============================= Training pipeline =============================
ℹ Pipeline: ['transformer', 'ner']
ℹ Initial learn rate: 0.0
E    #       LOSS TRANS...  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE 
---  ------  -------------  --------  ------  ------  ------  ------
  0       0        1027.60   2028.92    0.00    0.00    0.01    0.00
  0     200      225652.63  77443.33   17.55   20.90   15.12    0.18
  0     400       34799.92  12790.88   69.73   69.77   69.69    0.70
  0     600       16755.79   9699.92   74.23   69.75   79.32    0.74
  1     800        5509.15   8061.05   77.48   72.91   82.65    0.77
  1    1000        5524.08   8379.61   78.38   72.42   85.41    0.78
  1    1200        4490.30   7921.10   81.05   77.75   84.65    0.81
  2    1400        4319.48   6579.05   81.78   79.93   83.72    0.82
  2    1600        3331.55   6981.83   80.43   72.27   90.67    0.80
  2    1800        2940.46   6159.03   82.06   75.51   89.86    0.82
  3    2000        2940.73   5604.61   84.07   83.55   84.58    0.84
  3    2200        5573.14   6000.54   85.11   82.78   87.57    0.85
  3    2400        2792.99   5804.08   85.59   83.59   87.69    0.86
...
 22   13600         236.77    340.90   97.73   97.00   98.47    0.98
 22   13800         221.60    333.28   98.20   97.99   98.42    0.98
 ```