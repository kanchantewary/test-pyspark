@pytest.fixture()
def business_rdd(spark_context):
return spark_context.parallelize(business_table_data, 1).map(parse_line)
