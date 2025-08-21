from datetime import datetime

from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.database import get_database, DB_TZ
from vnpy.trader.constant import Interval
from vnpy.trader.object import BarData, HistoryRequest
from vnpy.trader.utility import extract_vt_symbol
from vnpy.trader.setting import SETTINGS

datafeed = get_datafeed()
database = get_database()

# 要下载数据的合约代码
vt_symbols = [
    "IF2501.CFFEX",
    "IF2502.CFFEX",
    "IF2503.CFFEX",
    "IH2501.CFFEX",
    "IH2502.CFFEX",
    "IH2503.CFFEX",
    "IC2501.CFFEX",
    "IC2502.CFFEX",
    "IC2503.CFFEX",
    "IM2501.CFFEX",
    "IM2502.CFFEX",
    "IM2503.CFFEX",
]

# 要下载数据的起止时间
start = datetime(2025, 1, 1, tzinfo=DB_TZ)
end = datetime(2025, 3, 30, tzinfo=DB_TZ)

for vt_symbol in vt_symbols:
    # 合约代码、交易所
    symbol, exchange = extract_vt_symbol(vt_symbol)

    req: HistoryRequest = HistoryRequest(symbol=symbol,
                                         exchange=exchange,
                                         start=start,
                                         end=end,
                                         interval=Interval.DAILY)  # 注意：按天的可以下载，其他需要积分

    # 从数据服务下载数据
    bars: list[BarData] = datafeed.query_bar_history(req)

    if bars:
        database.save_bar_data(bars)
        print(f"下载数据成功：{vt_symbol}，总数据量：{len(bars)}")
    else:
        print(f"下载数据失败：{vt_symbol}")
