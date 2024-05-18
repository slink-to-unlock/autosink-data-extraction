from autosink_data_extraction.backends.gdown import GDownBackend

if __name__ == '__main__':
    url = 'https://drive.google.com/drive/folders/1kDuFAmqoBAVh3R1zAGtmHKl-o5v7tKCT'

    # GDown 예시
    gdown_backend = GDownBackend(url)
    gdown_backend.to_local()
