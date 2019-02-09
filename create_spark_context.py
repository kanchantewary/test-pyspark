@pytest.fixture(scope='session')
def spark_context():
   conf = SparkConf().setMaster('local[2]').setAppName('pytest-pyspark-local-testing')
   sc = SparkContext(conf=conf)
yield sc
