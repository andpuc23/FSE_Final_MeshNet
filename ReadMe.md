## Introduction
This repository is not an original official implementation of the work, but a refactored codebase.
Performed within the FSE coursework at Skoltech.
The repository is a modification of [original repo](https://github.com/iMoonLab/MeshNet).
We make the project easier to use and less irritating to setup.

As authors mention, please cite them in your research:

```
@article{feng2018meshnet,
  title={MeshNet: Mesh Neural Network for 3D Shape Representation},
  author={Feng, Yutong and Feng, Yifan and You, Haoxuan and Zhao, Xibin and Gao, Yue},
  journal={AAAI 2019},
  year={2018}
}
```

## Quickstart
`scripts` directory contains shell scripts for the main subroutines:
1. install_libs.sh downloads all required python libraries, listed in requirements.txt 
2. get_dataset.sh to download the dataset from Google.Drive
3. preprocess_data.sh does the data processing - unzips downloaded archive, re-encodes the mesh models, etc.
4. train_model.sh performs the model training
5. eval_model.sh checks model performance

To use the project as-is run all the .sh files sequentially __or__
run do_all_the_stuff.sh, which has all the scripts inside

## Development

List of packages and their contents:

- config
  - .yaml configurations for training and tests of the model
  - config.py loads the configurations
- data
  - ModelNet40.py contains the model class and its constructor
  - preprocess.py iterates over dataset and performs transformations
- doc
  - has a .png picture used in README_base.md
- scripts
  - contains 5 .sh files, their actions are listed above
- test
  - has .py files with different tests for the project
- utils
  - GetDataset.py is utility function to download files from Google.Drive by `requests` library
  - retrival.py has some shitcode inside and I can not really understand what does it do

### List of good deeds

- [x] make a plan
- [x] create script files
- [x] fill scripts
- [x] docker file, docker image
- [ ] build system (do we need it?)
- [ ] tests - in progress
- [x] GitHub actions - in progress
- [x] ReadMe


### Checking procedure
1. Clone repo, check dependencies are pulled
2. Read readme
3. Launch docker
    1. pull image from dockerhub
    2. build image locally
4. Run tests
5. Run entry-points