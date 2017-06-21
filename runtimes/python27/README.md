# Python 2.7 runtime

## Description
 * ubuntu 14.04
 * python 2.7.6
 * python-pip
 * python-setuptools
 * python-dev

## Usage

In order to use this runtime a `new_module.py` and a `requirements.txt` must exist in a zip file.

the `new_module.py` should implement a `main` function that expects a payload of any type, `string`, `dict`, `int`, etc.

    def main(payload=None):
        return payload

other files different that `new_module.py` and `requirements.txt` will be removed

## How it works

When a container runs it will expected the payload to be send as environment variable:

    docker run -e pratai_payload='payload' -d name_of_container

inside the container the `server.py` file will load the new_module from the file system and expose it as a function.

`main` function will be wrapped within `server.py` to provide logging and response functionality to the function.