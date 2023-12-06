import argparse
import sys

import ducttape


def main():
    args = _parse_args()
    output_file = _open_output(args)
    output = ducttape.script(
        args.script,
        add_python_modules=args.add_python_module,
        add_python_paths=args.add_python_path,
        python_binary=args.python_binary,
        copy_shebang=args.copy_shebang,
        public_key=args.public_key,
        keygen=args.keygen,
    )
    if output is None:
        return
    output_file.write(output)


def _open_output(args):
    if args.output_file is None:
        return sys.stdout
    else:
        return open(args.output_file, "w")


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("script")
    parser.add_argument("--add-python-module", action="append", default=[])
    parser.add_argument("--add-python-path", action="append", default=[])
    parser.add_argument("--python-binary")
    parser.add_argument("--output-file")
    parser.add_argument("--copy-shebang", action="store_true")
    parser.add_argument("keygen", action="store_true")
    parser.add_argument("--public-key")
    return parser.parse_args()


if __name__ == "__main__":
    main()
