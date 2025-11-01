import os
import tempfile

from fileGuard import FileGurad


def error():
    with tempfile.TemporaryDirectory() as tp:
        f = os.path.join(tp, "test.txt")
        with open(f, "w") as ff:
            ff.write("旧文件")
        try:
            with FileGurad(f):
                with open(f, "w") as ff:
                    ff.write("新文件")
                raise RuntimeError("异常")

        except RuntimeError:
            pass
        with open(f) as ff:
            assert ff.read() == "旧文件"
    print("完成")


def correct():
    with tempfile.TemporaryDirectory() as tp:
        f = os.path.join(tp, "test.txt")
        with open(f, "w") as ff:
            ff.write("旧")

        with FileGurad(f):
            with open(f, "w") as ff:
                ff.write("新")

        with open(f) as ff:
            assert ff.read() == "新"
        assert not os.path.exists(f + ".bak")

    print("ok")


if __name__ == "__main__":
    correct()
    error()
