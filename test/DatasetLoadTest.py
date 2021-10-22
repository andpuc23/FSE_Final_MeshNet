import os.path
import unittest
import subprocess


class TestLoadDataset(unittest.TestCase):
    def setUp(self) -> None:
        subprocess.run(['cd ../scripts'])
        subprocess.run(['./get_dataset.sh'])

    def test_data_loaded(self):
        assert os.path.exists('../data/ModelNet40_MeshNet.zip')

    def tearDown(self) -> None:
        subprocess.run(['cd ../data'])
        subprocess.run(['rm', 'ModelNet40_MeshNet.zip'])


if __name__ == '__main__':
    unittest.main()
