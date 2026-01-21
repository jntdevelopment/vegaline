import argparse
import base64
import gzip
import hashlib
import hmac
import logging
import time
from pathlib import Path

import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

BC_B64 = "I/tXPXJPc8yxl+rwkztZJ2oL0poD34RvHhkLXPu7moY="
META = {
    "iv_client": "dcf5Ctak0R7GymMqxqG1IQ==",
    "clientKey": "SzPESg7dXdc+0hxwhA2paNfKRsiaze5C/GhHVVBlkxMbizFD5SflLh9np6N3YITt",
    "hmac": "AgybnDxOnae5dcoqGuNSPkdbG2JkaDJTbKSfC1IMOSQ=",
    "iv_server": "LP0X9bkVEHnPEhfAo9sU/w==",
}
SEED = 13640759039921189105

def pkcs7_unpad(data: bytes, block: int = 16) -> bytes:
    pad = data[-1]
    if pad < 1 or pad > block:
        raise ValueError("invalid padding")
    if data[-pad:] != bytes([pad]) * pad:
        raise ValueError("invalid padding")
    return data[:-pad]


def derive_master_key(bytecode: bytes, seed: int) -> bytes:
    n = len(bytecode)
    indices = np.arange(n, dtype=np.int64)
    shifts = (indices * 7) % 48

    keystream = ((np.uint64(seed) >> shifts.astype(np.uint64)) & 0xFF).astype(np.uint8)
    
    bc_arr = np.frombuffer(bytecode, dtype=np.uint8)
    return (bc_arr ^ keystream).tobytes()


def aes_cbc(key: bytes, iv: bytes):
    try:
        from Crypto.Cipher import AES
    except ModuleNotFoundError:
        from Cryptodome.Cipher import AES
    return AES.new(key, AES.MODE_CBC, iv)


def decrypt_key(enc_key: bytes, iv: bytes, master: bytes) -> bytes:
    cipher = aes_cbc(master, iv)
    plaintext = cipher.decrypt(enc_key)
    return pkcs7_unpad(plaintext)


def decrypt_payload(enc: bytes, iv: bytes, key: bytes) -> bytes:
    cipher = aes_cbc(key, iv)
    plaintext = pkcs7_unpad(cipher.decrypt(enc))
    try:
        return gzip.decompress(plaintext)
    except OSError:
        return plaintext


def verify_hmac(data: bytes, mac: bytes, key: bytes) -> None:
    calc = hmac.new(key, data, hashlib.sha256).digest()
    if calc != mac:
        raise ValueError("HMAC mismatch; encrypted payload may be corrupted")


def load_iso(path: Path) -> tuple[bytes, bytes, bytes]:
    start = time.perf_counter()
    raw = path.read_bytes()
    elapsed = time.perf_counter() - start
    log.info(f"[+] read iso {path} ({len(raw):,} bytes) in {elapsed:.3f}s")
    return raw[:16], raw[-32:], raw[16:-32]


def main() -> None:
    parser = argparse.ArgumentParser(description="Decrypt vRes2.iso jar")
    parser.add_argument("--iso", type=Path, default=Path("vRes2.iso"))
    parser.add_argument("--out", type=Path, default=Path("vRes2.jar"))
    args = parser.parse_args()

    total_start = time.perf_counter()
    log.info(f"[+] start decrypt {args.iso} -> {args.out}")

    bytecode = base64.b64decode(BC_B64)
    enc_client = base64.b64decode(META["clientKey"])
    iv_server = base64.b64decode(META["iv_server"])
    iv_client = base64.b64decode(META["iv_client"])
    hmac_key = base64.b64decode(META["hmac"])

    _, mac, enc = load_iso(args.iso)
    verify_hmac(enc, mac, hmac_key)
    log.info("[+] hmac verified")

    step = time.perf_counter()
    master = derive_master_key(bytecode, SEED)
    log.info("[+] master key derived")

    client_key = decrypt_key(enc_client, iv_server, master)
    log.info("[+] client key decrypted")

    payload = decrypt_payload(enc, iv_client, client_key)
    log.info(f"[+] payload decrypted ({len(payload):,} bytes)")

    args.out.write_bytes(payload)
    log.info(f"[+] wrote {args.out} ({args.out.stat().st_size:,} bytes)")
    log.info(f"[+] master key: {master.hex()}")
    log.info(f"[+] client key: {client_key.hex()}")

    total_elapsed = time.perf_counter() - total_start
    log.info(f"[+] done in {total_elapsed:.3f}s")


if __name__ == "__main__":
    main()