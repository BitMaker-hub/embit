import sys
from .test_ecc import *
from .test_base58 import *
from .test_bech32 import *
from .test_bip32 import *
from .test_psbt import *
from .test_bip39 import *
from .test_slip39 import *
from .test_descriptor import *
from .test_psbtview import *
from .test_taproot import *
from .test_script import *

if sys.implementation.name != "micropython":
    from .test_ripemd160 import *
    from .test_bindings import *
    from .test_threading import *
