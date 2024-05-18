# 서드파티
import gdown

# 프로젝트
from autosink_data_extraction.backends.base import BaseBackend


class GDownBackend(BaseBackend):

    def login(self):
        # GDown does not require login
        pass

    def logout(self):
        # GDown does not require logout
        pass

    def download_archive(self):
        folder_id = self.folder_url.split('/')[-1]
        # gdown.download_folder 압축 해제 위치를 직접 지정
        gdown.download_folder(id=folder_id, output=self.extract_to, quiet=False, use_cookies=False)

    def extract_archive(self):
        # GDownBackend의 경우 이미 download_folder에서 압축 해제가 수행되므로 이 메서드는 빈 동작을 정의
        print(f'Content is already extracted to {self.extract_to}')
