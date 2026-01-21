import argparse
import base64
import gzip
import json
from pathlib import Path

PHRASE = b"AJSDKAJSDLKASJDLKZXMC,"


def decode_meta(data_path: Path) -> dict:
    buf = bytearray(data_path.read_bytes())
    for i, b in enumerate(buf):
        buf[i] = b ^ PHRASE[i % len(PHRASE)]
    decompressed = gzip.decompress(buf)
    return json.loads(decompressed.decode())


def load_bc_seed(key_path: Path) -> tuple[str, int]:
    obj = json.loads(key_path.read_text())
    return obj[".byteCode"][0], int(obj[".byteCodeKey"])


def main() -> None:
    parser = argparse.ArgumentParser(description="show current META/BC/SEED from data.bin and KeyValue2.json")
    parser.add_argument("--data", type=Path, default=Path("boiler/data.bin"))
    parser.add_argument("--key", type=Path, default=Path("boiler/KeyValue2.json"))
    args = parser.parse_args()

    meta = decode_meta(args.data)
    bc_b64, seed = load_bc_seed(args.key)

    print("BC_B64=", bc_b64)
    print("SEED=", seed)
    print("META=", json.dumps(meta, separators=(",", ":")))


if __name__ == "__main__":
    main()
