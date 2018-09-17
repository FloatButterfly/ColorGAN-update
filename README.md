# COLORGAN
This is codes for Unsupervised Diverse Colorization via Generative Adversarial Networks

## Requirement
tensorflow
numpy  
scipy  
Pillow  
cv2  
cloudpickle

## Usage
### Prepare data  
make sure all images in your dataset are 3-channels image (you can use clean_dataset to clean)
Maximum center crop the data and reshape into 64*64,  (you can use resize file)
put reshaped data into data/ your_name/
### Train  
run train_lsun_wgan.sh for shortcut  
or adjust settings by:
```
python main_wgan.py --is_train=True --some_paramter=some_value
```  
### Test  
run test_lsun_wgan.sh for shortcut  
or adjust settings by:
```
python main_wgan.py --is_train=False --some_paramter=some_value
```  


