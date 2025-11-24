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
        if v < 0:
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


def add_cmd(args):
    global id, accountDataBase
    rec = {
        "id": id,
        "date": args.date or dt.date.today(),
        "desc": args.desc,
        "amount": args.amount,
    }
    accountDataBase.append(rec)
    id += 1
    print("✅ 已记录:", rec)
    print("[ADD] 全局列表长度", len(accountDataBase))


def list_cmd(args):
    print(
        "[LIST] 进入函数，全局长度=", len(accountDataBase), "args.number=", args.number
    )
    rows = accountDataBase if args.number < 0 else accountDataBase[-args.number :]
    if not rows:
        print("无记录")
        return
    print(f"{'ID':<4}{'Date':<12}{'Amount':>8}Desc")
    for r in rows:
        print(f"{r['id']:<4}{r['date']}{r['amount']:>8.2f}{r['desc']}")


def stats_cmd(args):
    if args.month:
        firstDay = dt.date.today().replace(day=1)
        nextMonth = (firstDay + dt.timedelta(days=32)).replace(day=1)
        total = sum(
            r["amount"] for r in accountDataBase if firstDay <= r["date"] < nextMonth
        )
        print(f"该月总消费{total:.2f}")
    else:
        total = sum(r["amount"] for r in accountDataBase)
        print(f"该月总消费{total:.2f}")


def del_cmd(args):
    global accountDataBase
    for indx, n in enumerate(accountDataBase):
        if n["id"] == args.id:
            accountDataBase.pop(indx)
            print("🗑️  已删除", n)
            return
    print(f"❌ 未找到 id={args.id}")


# 解析器配置

# 父解析器
parent = argparse.ArgumentParser(add_help=False)
parent.add_argument("-v", "--verbose", action="store_true", help="调试信息")

# 真正解析器入口
parser = argparse.ArgumentParser(
    prog="account-cli", description="命令行记账本", parents=[parent]
)
# 子命令文件夹，dest="command" 用来存用户敲了哪个子命令
sub = parser.add_subparsers(dest="command", required=True, help="子命令")


# 子命令

# add-----------
p_add = sub.add_parser("add", parents=[parent], help="添加一笔")
p_add.add_argument("-d", "--desc", required=True, help="消费描述")
p_add.add_argument("-a", "--amount", type=postive_float, required=True, help="消费总额")
p_add.add_argument(
    "--date", type=postive_datetime, default=dt.date.today(), help="日期(yyyy-mm-dd)"
)
p_add.set_defaults(func=add_cmd)

# list-----------
p_list = sub.add_parser("list", parents=[parent], help="列出记录")
p_list.add_argument("-n", "--number", type=int, default=10, help="最近 N 条（-1 全部）")
p_list.set_defaults(func=list_cmd)

# stats-----------
p_stats = sub.add_parser("stats", parents=[parent], help="统计")
g = p_stats.add_mutually_exclusive_group()
g.add_argument("--month", action="store_true", help="本月统计")
g.add_argument("--all", action="store_true", help="全部统计")
p_stats.set_defaults(func=stats_cmd)

# delete-----------
p_del = sub.add_parser("del", parents=[parent], help="删除")
p_del.add_argument("--id", type=int, required=True, help="记录 ID")
p_del.set_defaults(func=del_cmd)


def main(argv=None):
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
