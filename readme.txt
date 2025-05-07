This is code for "ECINFusion: A Novel Explicit Channel-wise Interaction Network for Unified Multi-modal Medical Image Fusion(TCSVT'24)"

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

The pre-trained on CT-MRI: https://drive.google.com/file/d/1Wpr1T16acHboDGSlZzZGabroygr2U7OP/view?usp=drive_link


The pre-trained on PET-MRI: https://drive.google.com/file/d/1acy75A2UHXHUY1zFxlYJLpvC2x2Nf3SX/view?usp=drive_link




@ARTICLE{ECINFusion,
  author={Wei, Xinjian and Qiu, Yu and Xu, Xiaoxuan and Xu, Jing and Mei, Jie and Zhang, Jun},
  journal={IEEE Transactions on Circuits and Systems for Video Technology}, 
  title={ECINFusion: A Novel Explicit Channel-Wise Interaction Network for Unified Multi-Modal Medical Image Fusion}, 
  year={2025},
  volume={35},
  number={5},
  pages={4011-4025},
  keywords={Biomedical imaging;Image fusion;Adaptation models;Feature extraction;Transformers;Magnetic resonance imaging;Convolution;Transforms;Single photon emission computed tomography;Semantics;Multi-modal medical image fusion;multi-modal image fusion;multi-modal interaction;feature fusion;transformer},
  doi={10.1109/TCSVT.2024.3516705}}



Thanks for the work of MATR.
