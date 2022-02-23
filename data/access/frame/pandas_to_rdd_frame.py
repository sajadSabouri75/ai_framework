from data.access.frame.frame import Frame
from helpers.exceptions import frame_exceptions as excepts
import pandas as pd
from pyspark.sql import SparkSession


class PandasRDDFrame(Frame):
    def __init__(self, **kwargs):
        super(PandasRDDFrame, self).__init__(**kwargs)
        self._pandas_object = kwargs['pandas'] if 'pandas' in kwargs else None
        self.check_on_construction_inputs()

    def check_on_construction_inputs(self):
        try:
            if self._pandas_object is None:
                raise excepts.NoPandasObject(self._loggers)
            if not isinstance(self._pandas_object, pd.core.frame.DataFrame):
                raise excepts.NoPandasType(self._loggers)
        except excepts.FrameException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalFrameException(self._loggers).evoke(e)

    def frame(self):
        for logger in self._loggers:
            logger.print_internal_message('Framing initiated ...')
        try:
            spark_session = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
            spark_session.sparkContext.setLogLevel("FATAL")
            spark_dataframe = spark_session.createDataFrame(self._pandas_object)
            spark_dataframe.printSchema()
        except Exception as e:
            excepts.VitalFrameException(self._loggers).evoke(e)
        for logger in self._loggers:
            logger.confirm_framing()
        return spark_dataframe
