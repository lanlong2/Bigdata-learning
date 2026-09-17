# 学习起步模板：尚未实现清洗逻辑。
# 先读上一级文件夹的“任务书.md”，不要把验收数字直接写成答案。
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_DIR / "data" / "示例订单.csv"
RESULT_DIR = PROJECT_DIR / "results"

# TODO 1：读取 INPUT_FILE。
# TODO 2：校验字段，记录无效行及原因。
# TODO 3：按订单编号去重。
# TODO 4：汇总数量、销售额和商品销量。
# TODO 5：创建 RESULT_DIR，保存 CSV 和 JSON。
# TODO 6：用任务书里的边界情况检验程序。
