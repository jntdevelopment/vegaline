import os
import logging
import time
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

def decrypt(input_file, output_file):
    xor_key = b'XOR_SIMPLE_KEY'

    if not os.path.exists(input_file):
        log.error(f"[!] file '{input_file}' was not found")
        return

    try:
        start = time.perf_counter()

        log.info(f"[+] reading {input_file}")
        with open(input_file, 'rb') as f_in:
            edata = np.frombuffer(f_in.read(), dtype=np.uint8)

        log.info(f"[+] decrypting {input_file}")
        key_len = len(xor_key)
        key_arr = np.frombuffer(xor_key, dtype=np.uint8)
        full_key = np.tile(key_arr, (len(edata) // key_len) + 1)[:len(edata)]
        ddata = edata ^ full_key

        log.info(f"[+] writing {output_file}")
        with open(output_file, 'wb') as f_out:
            f_out.write(ddata.tobytes())

        elapsed = time.perf_counter() - start
        log.info(f"[+] success decrypt '{input_file}' -> '{output_file}' in {elapsed:.3f}s ({len(ddata):,} bytes)")

    except IOError as e:
        log.error(f"[!] error during file operation {e}")
    except Exception as e:
        log.error(f"[!] unexpected error {e}")

if __name__ == '__main__':
    ifl = 'vRes1.iso'
    ofl = 'vRes1.jar'

    decrypt(ifl, ofl)