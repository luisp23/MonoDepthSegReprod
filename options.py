# Copyright Niantic 2019. Patent Pending. All rights reserved.
#
# This software is licensed under the terms of the Monodepth2 licence
# which allows for non-commercial use only, the full terms of which are made
# available in the LICENSE file.

from __future__ import absolute_import, division, print_function

import os
import argparse

file_dir = os.path.dirname(__file__)  # the directory that options.py resides in


class MonodepthOptions:
     def __init__(self):
          self.parser = argparse.ArgumentParser(description="Monodepthv2 options")

          # PATHS
          self.parser.add_argument("--data_path",
                                   type=str,
                                   help="path to the training data",
                                   default=os.path.join(file_dir, "kitti_data"))
          
          self.parser.add_argument("--log_dir",
                                   type=str,
                                   help="log directory",
                                   default=os.path.join(os.path.expanduser("~"), "tmp"))
          
          
          
          # mask and depth validation arguments
          self.parser.add_argument("--val_log_dir",
                                   type=str,
                                   help="depth and masking validation log directory",
                                   default=os.path.join(os.path.expanduser("~"), "depth_masking_validation"))

          self.parser.add_argument("--num_val_batches",
                                   type=int,
                                   help="number of batches to validate for",
                                   default=1)
          
          
          
          
          # TRAINING options
          self.parser.add_argument("--model_name",
                                   type=str,
                                   help="the name of the folder to save the model in",
                                   default="mdp")
          
          self.parser.add_argument("--split",
                                   type=str,
                                   help="which training split to use",
                                   choices=["eigen_zhou", "eigen_full", "odom", "benchmark"],
                                   default="eigen_zhou")
          
          self.parser.add_argument("--dataset",
                                   type=str,
                                   help="dataset to train on",
                                   default="kitti",
                                   choices=["kitti", "kitti_odom", "kitti_depth", "kitti_test"])
          
          self.parser.add_argument("--png",
                                   help="if set, trains from raw KITTI png files (instead of jpgs)",
                                   action="store_true")
          self.parser.add_argument("--height",
                                   type=int,
                                   help="input image height",
                                   default=192)
          self.parser.add_argument("--width",
                                   type=int,
                                   help="input image width",
                                   default=640)
          
          # TODO: Smooth coefficient
          self.parser.add_argument("--disparity_smoothness",
                                   type=float,
                                   help="disparity smoothness weight",
                                   default=1e-3)
          
          self.parser.add_argument("--min_depth",
                                   type=float,
                                   help="minimum depth",
                                   default=0.1)
          self.parser.add_argument("--max_depth",
                                   type=float,
                                   help="maximum depth",
                                   default=80.0)
          
          self.parser.add_argument("--frame_ids",
                                   nargs="+",
                                   type=int,
                                   help="frames to load",
                                   default=[0, -1, 1])

          # OPTIMIZATION options
          self.parser.add_argument("--batch_size",
                                   type=int,
                                   help="batch size",
                                   default=12)
          
          self.parser.add_argument("--learning_rate",
                                   type=float,
                                   help="learning rate",
                                   default=1e-4)
          
          self.parser.add_argument("--num_epochs",
                                   type=int,
                                   help="number of epochs",
                                   default=20)
          
          self.parser.add_argument("--scheduler_step_size",
                                   type=int,
                                   help="step size of the scheduler",
                                   default=15)

          # ABLATION options
          self.parser.add_argument("--num_K",
                                   type=int,
                                   help="number of masks and poses to predict",
                                   default=5)
     
          # SYSTEM options
          self.parser.add_argument("--num_workers",
                                   type=int,
                                   help="number of dataloader workers",
                                   default=8)

          # LOADING options
          self.parser.add_argument("--load_weights_folder",
                                   type=str,
                                   help="name of model to load", 
                                   default=None)
          
          self.parser.add_argument("--models_to_load",
                                   nargs="+",
                                   type=str,
                                   help="networks to load",
                                   default=["depth_encoder", "depth_decoder", "pose_mask_encoder", "mask_decoder", "pose_decoder"])

          # LOGGING options
          self.parser.add_argument("--log_frequency",
                                   type=int,
                                   help="number of batches between each tensorboard log",
                                   default=250)
          
          self.parser.add_argument("--save_frequency",
                                   type=int,
                                   help="number of epochs between each save",
                                   default=1)

          
          
          # TODO: Used to do evaluation AFTER training; used in evaluate_depth.py in monodepth2 codebase 
          
          # EVALUATION options
          # Not needed? 
          
          # self.parser.add_argument("--eval_stereo",
          #                          help="if set evaluates in stereo mode",
          #                          action="store_true")
          
          
          self.parser.add_argument("--eval_mono",
                                   help="if set evaluates in mono mode",
                                   action="store_true")
          
          
          self.parser.add_argument("--disable_median_scaling",
                                   help="if set disables median scaling in evaluation",
                                   action="store_true")
          self.parser.add_argument("--pred_depth_scale_factor",
                                   help="if set multiplies predictions by this number",
                                   type=float,
                                   default=1)
          self.parser.add_argument("--ext_disp_to_eval",
                                   type=str,
                                   help="optional path to a .npy disparities file to evaluate")
          self.parser.add_argument("--eval_split",
                                   type=str,
                                   default="eigen",
                                   choices=[
                                        "eigen", "eigen_benchmark", "benchmark", "odom_9", "odom_10"],
                                   help="which split to run eval on")
          self.parser.add_argument("--save_pred_disps",
                                   help="if set saves predicted disparities",
                                   action="store_true")
          self.parser.add_argument("--no_eval",
                                   help="if set disables evaluation",
                                   action="store_true")
          self.parser.add_argument("--eval_eigen_to_benchmark",
                                   help="if set assume we are loading eigen results from npy but "
                                        "we want to evaluate using the new benchmark.",
                                   action="store_true")
          self.parser.add_argument("--eval_out_dir",
                                   help="if set will output the disparities to this folder",
                                   type=str)
          self.parser.add_argument("--post_process",
                                   help="if set will perform the flipping post processing "
                                        "from the original monodepth paper",
                                   action="store_true")

     def parse(self):
          self.options = self.parser.parse_args()
          return self.options
