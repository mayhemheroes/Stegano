#! /usr/bin/python3

import atheris
import sys
import io
import PIL

with atheris.instrument_imports():
    import stegano

def TestOneInput(data):
    try:
        stegano.lsb.hide(PIL.Image.open(io.BytesIO(data)).convert("RGBA"), "A")
    except PIL.UnidentifiedImageError:
        pass
    except PIL.Image.DecompressionBombError:
        pass
    except ValueError:
        pass
    except OSError:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
