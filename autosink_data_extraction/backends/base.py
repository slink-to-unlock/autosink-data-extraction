# 내장
import abc
import zipfile
import tarfile


class BaseBackend(metaclass=abc.ABCMeta):

    def __init__(self, folder_url):
        self.folder_url = folder_url
        self._archive_path = None
        self._extract_to = 'validation-candidate-data'

    @property
    def archive_path(self):
        return self._archive_path

    @archive_path.setter
    def archive_path(self, value):
        self._archive_path = value

    @property
    def extract_to(self):
        return self._extract_to

    @abc.abstractmethod
    def login(self):
        pass

    @abc.abstractmethod
    def logout(self):
        pass

    @abc.abstractmethod
    def download_archive(self):
        pass

    def extract_archive(self):
        if zipfile.is_zipfile(self.archive_path):
            with zipfile.ZipFile(self.archive_path, 'r') as z:
                z.extractall(path=self.extract_to)
                print(f'Extracted {self.archive_path} into directory {self.extract_to}')
        elif tarfile.is_tarfile(self.archive_path):
            with tarfile.open(self.archive_path, 'r:*') as tar:
                tar.extractall(path=self.extract_to)
                print(f'Extracted {self.archive_path} into directory {self.extract_to}')
        else:
            raise ValueError(f'The file at {self.archive_path} is not a supported archive format.')

    def to_local(self):
        self.login()
        self.download_archive()
        self.extract_archive()
        self.logout()
