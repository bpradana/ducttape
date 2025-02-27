# DuctTape
DuctTape is a tool for packaging, encrypting, and obfuscating your python scripts.
It is a fork of [stickytape](https://github.com/mwilliamson/stickytape) with added encryption and obfuscation features.

## Features
- Package your python scripts into a single file
- Encrypt your python scripts using RSA
- Obfuscate your python scripts

## Installation
The easiest way to install ducttape is using pip:
```bash
$ pip install pyducttape
```
But you can also install DuctTape from source:
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

## Example
You can find an example of original script [here](example/hello) and the ducttaped one [here](example/ducttaped.py), but you won't be able to run it because it's encrypted with my public key.

To run the example, you need to generate your own key pair and encrypt the script with your public key.
```bash
$ ducttape --keygen
$ ducttape example/hello/main.py --public-key=public.pem > example/ducttaped.py
$ python example/ducttaped.py
```

## License
DuctTape is licensed under the [BSD 2-Clause License](LICENSE)

## Credits
DuctTape is a fork of [Michael Williamson](https://github.com/mwilliamson)'s amazing project, [stickytape](https://github.com/mwilliamson/stickytape)
