# MonoDepthSegReprod
Final project for CS 7643 Deep Learning focusing on reproducing the results detailed in "Self-Supervised Monocular Scene Decomposition and Depth Estimation" - S. Safadoust,  F. Guney (2021)

## Dependencies (Current)
- `torchvision-0.11.1`
- `pytorch-1.10.0`
- `numpy-1.21.2`

## Training and Validation
Command for Training: 
- `python train.py --png --data_path ../kitti_data --load_weights_folder /home/luis/backup_model_run/mdp_run5/networks/weights_5/`

Command for Evaluation:
- `python depth_masking_validation.py --png --data_path ../kitti_data --load_weights_folder /home/luis/backup_model_run/mdp_run6/networks/weights_4/ --num_val_batches=2`

Command for Viewing Logs:
- `tensorboard --logdir=<dir_of_log>`


## References
This codebase reproduces the MonoDepthSeg architecture described in the following work:

> **Self-Supervised Monocular Scene Decomposition and Depth Estimation**
>
> [Sadra Safadoust](ssafadoust20@ku.edu.tr), [Fatma Güney](https://mysite.ku.edu.tr/fguney/)
>
> [3DV 2021 (arXiv pdf)](https://arxiv.org/abs/2110.11275)

No public code implementations for this work currently exist.

---

This codebase also uses model architectures and utility functions from the following work per their non-commercial use license: 
> **Digging into Self-Supervised Monocular Depth Prediction**
>
> [Clément Godard](http://www0.cs.ucl.ac.uk/staff/C.Godard/), [Oisin Mac Aodha](http://vision.caltech.edu/~macaodha/), [Michael Firman](http://www.michaelfirman.co.uk) and [Gabriel J. Brostow](http://www0.cs.ucl.ac.uk/staff/g.brostow/)
>
> [ICCV 2019 (arXiv pdf)](https://arxiv.org/abs/1806.01260)
>
> [nianticlabs/monodepth2 (Github)](https://github.com/nianticlabs/monodepth2)
> 
> Copyright © Niantic, Inc. 2018. Patent Pending.

