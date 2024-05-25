# vscode-py-template

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

环境是基于 MacOS、Linux。

## `Makefile`

`Makefile` 具有以下功能。

### `make lint`

- 若要使用 `.vscode` 设置，请安装 `pylint` 扩展。
- 通过覆盖 linter 的默认设置与在 `pyproject.toml` 文件中指定的选项，对代码进行 lint。

### `make format`

- 使用 google 的 `yapf` 作为格式化工具。
- 通过覆盖 `yapf` 格式化器的默认设置与在 `pyproject.toml` 文件中指定的选项，对代码进行格式化。
- 若要使用 `.vscode` 设置，请安装 `yapf` 扩展。

### `make test`

- 使用 `unittest` 进行测试。
- 支持 `test_*.py` 和 `*_test.py` 模式。
- 测试文件必须通过 `__init__.py` 连接到测试文件所在的位置。

### `make publish`

- 编写 `~/.pypirc` 文件如下。
    ```
    [pypi]
    username = __token__
    password = pypi-这个那个 # 请获取个人 API 令牌并填写。
    ```
- 运行此命令将使用 `flit` 将软件包推送到 PyPI 公共注册表。
- 通过之前指定的名称 `myproject`（假名），上传后，任何人都可以通过 `python3 -m pip install myproject` 安装并使用软件包。