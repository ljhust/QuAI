from backtrader import feed
import pandas as pd
from datetime import date, datetime
from backtrader.utils import date2num


class DayCSVData(feed.CSVDataBase):
    """
    Parses pre-downloaded CSV data, which is day quotation of Chinese market.

    Specific parameters:
        - "Unnamed: 0": useless col

        - "close":  close price

        - "date"

        - "high"

        - "low"

        - "open"

        - "outstanding_share"

        - "symbol"

        - "turnover"

        - "volume"
    """

    lines = ('turnover', 'outstanding_share', 'symbol')

    params = (
        ('close', 2),
        ('datetime', 3),
    )

    # def start(self):
    #     super(DayCSVData, self).start()

    def _loadline(self, linetokens):
        itoken = iter(linetokens)

        # pre places token are useless
        # next(itoken)
        # next(itoken)



        dttxt = next(itoken)
        dt = datetime(int(dttxt[0:4]), int(dttxt[5:7]), int(dttxt[8:]))
        self.lines.datetime[0] = date2num(dt)

        self.lines.open[0] = float(next(itoken))
        self.lines.high[0] = float(next(itoken))
        self.lines.low[0] = float(next(itoken))
        self.lines.close[0] = float(next(itoken))
        self.lines.volume[0] = float(next(itoken))
        self.lines.outstanding_share[0] = float(next(itoken))
        self.lines.turnover[0] = float(next(itoken))

        return True

