from data.access.frame.frame import Frame
from helpers.exceptions import frame_exceptions as excepts
from helpers.exceptions import base_exceptions as base_excepts
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
                raise excepts.NoPandasObject
            if not isinstance(self._pandas_object, pd.core.frame.DataFrame):
                raise excepts.NoPandasType
        except excepts.FrameException as e:
            e.evoke()
        except Exception as e:
            excepts.VitalFrameException().evoke(e)

    def frame(self):
        spark_session = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
        spark_dataframe = spark_session.createDataFrame(self._pandas_object)
        spark_dataframe.printSchema()
        return spark_dataframe
