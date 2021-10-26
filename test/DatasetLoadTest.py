"""
testing the dataset is loaded
"""
import os
import unittest


class TestLoadDataset(unittest.TestCase):
    def setUp(self) -> None:
        """
        download dataset file
        :return:
        """
        os.system('cd ../scripts')
        os.system('./get_dataset.sh')

    def test_data_loaded(self):
        """
        the test itself
        :return:
        """
        assert os.path.exists('../data/ModelNet40_MeshNet.zip')

    def tearDown(self) -> None:
        """
        remove the file to be loaded
        :return:
        """
        os.system('cd ../data')
        os.system('rm ModelNet40_MeshNet.zip')


if __name__ == '__main__':
    unittest.main()
