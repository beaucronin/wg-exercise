# wg-exercise

## Install and Run

The server can be run locally, or as a Docker container.

### Local

A python virtual environment is recommended.

```
pip install -r requirements.txt
./run_local.sh
```

To specify a target directory, export the `ROOT_DIR` environment variable:

```
export ROOT_DIR=/some/dir
./run_local.sh
```

### Docker

Assuming Docker is properly configured and the service is running

```
docker build -t wg-exercise:latest .
docker run -d -p 5000:5000 wg-exercise:latest
```

To specify a target directory, use Docker's standard environment variable functionality to set the `ROOT_DIR` variable:

```
docker run -d -p 5000:5000 -e ROOT_DIR=/some/dir wg-exercise:latest
```

## Usage

Once the server has been brought up using one of the above methods, you can find it at http://localhost:5000/. 

## Test

The tests can be run via `./run_tests.sh`. They are incomplete, but should be expanded to include various other cases that ensure file size, ownership, and permissions are properly returned.