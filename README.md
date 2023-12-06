# DuctTape
DuctTape is a tool for packaging, encrypting, and obfuscating your python scripts.
It is a fork of [stickytape](https://github.com/mwilliamson/stickytape) with added encryption and obfuscation features.

## Features
- Package your python scripts into a single file
- Encrypt your python scripts using RSA
- Obfuscate your python scripts

## Installation
You can install DuctTape from source:
```bash
$ git clone https://github.com/bpradana/ducttape.git
$ cd ducttape
$ python setup.py install
```

## Usage
### Generate RSA key pair
This will generate `private.pem` and `public.pem` in your current directory
```bash
$ ducttape --keygen
```
### Encrypt
```bash
$ ducttape entrypoint.py --public-key=your_public_key.pem > encrypted.py
```
### Running encrypted script
make sure you have `private.pem` in your current directory
```bash
$ python encrypted.py
```

## License
DuctTape is licensed under the [BSD 2-Clause License](LICENSE)

## Credits
DuctTape is a fork of [Michael Williamson](https://github.com/mwilliamson)'s amazing project, [stickytape](https://github.com/mwilliamson/stickytape)
