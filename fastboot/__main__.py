"""
Invokes fastboot when run as a script.

Example: python -m fastboot
"""

import fastboot

if __name__ == "__main__":
    print("FastBoot " + fastboot.__version__)
