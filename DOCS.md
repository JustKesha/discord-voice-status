# Documentation

This file contains minimal project documentation,
mainly focusing on the things I find to be unclear at first glance.

## Configuration

The project can be configured using two files in the root directory:

1. **config.yaml** - [see it](config.yaml)
2. **.env** - has to be created manually, [see instructions](README.md#configuration)

> [!NOTE]
> Althought **.env** file is optional, it is highly suggested that you use both files for configuration.<br>
> As the env format is more suit for sensetive data, like the token required.

At startup the **config.yaml** and **.env** files are merged into a single python dictinary with **.env** file having a rewrite priority.<br>
Everything from the **.env** file is saved to dictinary under the "`env`" key.<br>
If **.env** file was not created or filled, those same values can be changed in **config.yaml** under the "`env`" field.

By default variables in **.env** have to start with the "`PY_DVS_`" prefix, those variables are saved to the result dictinary without the prefix.
This can be easily changed using optional arguments / __**kwargs__ for the `load_config(...)` method from [utils/config.py](src/utils/config.py) used in [main.py](src/main.py).
