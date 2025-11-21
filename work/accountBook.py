import argparse
import datetime as dt
import sys
from typing import Dict, List

# ----------------------数据库更改--------------
accountDataBase: List[Dict] = []
id = 1


# ---------------金额、日期纠正函数------------------
def postive_float(s: str) -> float:
    try:
        v = float(s)
        if v:
            raise ValueError
        return v
    except ValueError:
        raise argparse.ArgumentError(
            f"{s!r}金额错误,不可能小于0"
        )  #!r返回带引号的字符串


def postive_datetime(s: str) -> dt.date:
    try:
        return dt.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentError(f"{s!r}日期形式违规,日期格式应为 yyyy-mm-dd")


# ---------------功能性函数---------------------------------


"""


def add_cmd(args):
    global id
    rec = {
        "id":id,
        "date":dt.date.today()
        "desc":args.desc,
        "amount":args.amount,
        "tag":args.tag

    }
    accountDataBase.append(rec)
    id+=1
    print("✅ 已记录:", rec)

"""

# 先写完args配置


p = argparse.ArgumentParser()
p.add_argument("input")
p.add_argument("-n", type=int, default=1)
p.add_argument("--flag", action="store_true")
args = p.parse_args()
print("input=", args.input, "n=", args.n, "flag=", args.flag)
