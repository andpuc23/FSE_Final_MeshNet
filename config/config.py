import os
import os.path as osp
import yaml


def _check_dir(directory, make_dir=True):
    if not osp.exists(directory):
        if make_dir:
            print('Create directory {}'.format(directory))
            os.mkdir(directory)
        else:
            raise Exception('Directory not exist: {}'.format(directory))


def get_train_config(config_file='config/train_config.yaml'):
    with open(config_file, 'r') as f:
        cfg = yaml.load(f)

    _check_dir(cfg['dataset']['data_root'], make_dir=False)
    _check_dir(cfg['ckpt_root'])

    return cfg


def get_test_config(config_file='config/test_config.yaml'):
    with open(config_file, 'r') as f:
        cfg = yaml.load(f)

    _check_dir(cfg['dataset']['data_root'], make_dir=False)

    return cfg
