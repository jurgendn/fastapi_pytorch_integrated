# Web Service Framework

Based on the purpose of our projects, most of the time we provide API endpoints to other services or applications. Some popular Python Web frameworks are `Django, Flask, FastAPI`. For providing API endpoints only, I choose [`FastAPI`](https://fastapi.tiangolo.com/).

## Project Structure

The web structure is motivated and inherited by `Vue.js` structure

```bash
.
├── components
│   ├── ai_modules
│   │   └── recommend.py
│   ├── logger
│   │   ├── handlers.py
│   │   └── logger.py
│   └── middlewares
│       ├── depends.py
│       └── validation.py
├── config
│   ├── README.md
│   └── config.yaml
├── interfaces
│   ├── item.py
│   └── responses.py
├── routers
│   └── item.py
├── storage
│   └── logs
└── tests
│   └── tests_versions.py
├── config.py
├── app.py
├── requirements.txt
├── docker-compose.yml
```

The structure contains several main components:

1. Configuration
2. Package Dependency
3. Source code
4. Tests
5. Containerization

### Configuration

We use [`dynaconf`](https://www.dynaconf.com/) to parse and load configuration files. `Dynaconf` supports many file types, such as `yaml, json, toml, ini, py`, and `env`. For more detail, please read the documentation.

The `./config/` folder contains all the config files, and `dynaconf` will load configuration from these files in `./config.py`

```python
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['./config/settings.yaml'],
)
```

The `settings` variable now contains all the configurations that are declared in `./config/settings.yaml`

Note that, we may split the configuration into different files by some criteria.

### Package Dependencies

The package dependencies are defined in `pip-requirements`, in file name `requirements.txt` by default.

The `requirements.txt` should contain at least these packages:

```requirements.txt
pytests
uvicorn
fastapi
python-multipart
dynaconf
loguru
```

The 3 packages `fastapi, python-multipart, uvicorn` are used to run the web server. `Loguru` is used to make the logging task easier.

### Source code

All the source code is placed in `scr/` folder. Note that, we separate this application into smaller parts which means instead of writing all endpoints in one `FastAPI`.

We use `APIRouter` to manage endpoints by purpose. These routers are placed in `src/routers`.
The `src/components` use to contain all class definitions which are used in the project. We may include `ai_modules` for every AI inference model and related stuff, or add `logger`, `minio` based on demand.
The `src/interfaces` carries the data models, for example, the request data class or the response model in every endpoints.
To define the `APIRouter` in groups, we place the `APIRouter` definition in different files in the `src/routers`.

### Tests

We have a folder `test/` here containing all test cases, to check whether all the tests are satisfied or not.

The testing framework in this base project is [`PyTest`](https://docs.pytest.org/en/7.2.x/). Run all tests in the folder by placing this line in `./docker/startup.sh`:

```bash
pytest tests/
```

### Containerization

We run the training job on the Docker environment. To reduce the build time, I created my image. This custom image contains some basic packages:

- PyTorch and related modules
- opencv-headless
- CUDA

The image is placed on [Dockerhub](https://hub.docker.com/r/gr000a1/torch-gpu/tags)

```bash
.
|-- .docker
|   |-- Dockerfile
|   `-- startup.sh
|-- docker-compose.yml
|-- .env
|-- .dockerignore
```

This table gives the description of the file/folder in containerization.

| File/Folder         |                          Description |
| ------------------- | -----------------------------------: |
| ./docker            |   Includes Dockerfile and startup.sh |
| docker-compose.yaml |                  Docker Compose file |
| .dockerignore       | Define what not to copy to the image |
