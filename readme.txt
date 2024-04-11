This is code for "ECINFusion: A Novel Explicit Channel-wise Interaction Network for Unified Multi-modal Medical Image Fusion"

Dataset: All the multi-modal medical images are from the public dataset: Harvard, https://www.med.harvard.edu/AANLIB/home.html
And the other datasets are all list in our paper.

#Environment requirements reconmmended:
CUDA 11.3
python 3.7.10
pyTorch 1.12.1

#Please note that if you need color transforme, you can use different code like Matlab or Python. The color transform is form: 
https://github.com/yuliu316316/DPCN-Fusion

#How to train:
python Train.py

#How to test:
python Test.py


#pretrain-model
you can download pretrained models from the google drive: 
PET-MRI:
#How to train:
python Train.py
#How to test:
python Test.py



SPECT-MRI:
#How to train:
python Train.py
#How to test:
python Test.py

CT-MRI:
#How to train:
python Train.py
#How to test:
python Test.py

GFP-PC:
#How to train:
python Train.py
#How to test:
python Test.py

VIS-IR:
#How to train:
python Train.py
#How to test:
python Test.py

MEIF:
#How to train:
python Train.py
#How to test:
python Test.py

MFIF:
#How to train:
python Train.py
#How to test:
python Test.py

