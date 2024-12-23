### Create config.cfg file
```
python -m spacy init fill-config ./base_config.cfg ./config.cfg
```
### Train the model
```
python -m spacy train config.cfg --output ./output --paths.train ./train --paths.dev ./dev --gpu-id 0 # if using gpu to train
# python -m spacy train config.cfg --output ./output --paths.train ./train --paths.dev ./dev # if using cpu to train
```
