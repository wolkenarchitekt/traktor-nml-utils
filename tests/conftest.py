from pathlib import Path

from _pytest.config.argparsing import Parser


def pytest_addoption(parser: Parser):
    parser.addoption(
        "--nml-dir",
        action="append",
        default=[Path("./tests/fixtures")],
        type=Path,
        help="list of directories to search for NML files",
    )


def pytest_generate_tests(metafunc):
    nml_dir_option = metafunc.config.getoption("nml_dir")
    if "nml_dir" in metafunc.fixturenames:
        metafunc.parametrize("nml_dir", nml_dir_option)
