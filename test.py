
import os, sys, uuid
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from timedotc import timedotc

if __name__ == "__main__":
    secret_key = uuid.uuid4().hex
    auth = timedotc(
        method="sub",
        secret_key=secret_key,
    )

    target = auth.hash("0000")

    code = "1111"
    print(auth.verify(code, target))
