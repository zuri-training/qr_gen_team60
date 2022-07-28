import pathlib
import tomli

path = pathlib.Path(__file__).parent / "setup.toml"
with path.open(mode="rb") as my_conf:
    setup= tomli.load(my_conf)