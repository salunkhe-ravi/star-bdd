import pandas as pd
import pyodbc

from core.commons import CommonFunctions


class DBComparison():

    def connect_to_dbs():
        # DB1
        driver1 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL', sub_sub_key_name='DRIVER')
        # print('driver1 : ' + driver1)
        server1 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL', sub_sub_key_name='SERVER')
        # print('server1 : ' + server1)
        database1 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL',
                                                    sub_sub_key_name='DATABASE')
        # print('database1 : ' + database1)
        trusted_connection1 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL',
                                                              sub_sub_key_name='TRUSTED_CONNECTION')

        # print('trusted_connection1 : ' + trusted_connection1)

        # DB2
        driver2 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL', sub_sub_key_name='DRIVER')
        server2 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL', sub_sub_key_name='SERVER')
        database2 = 'db2;'
        trusted_connection2 = CommonFunctions().get_star_json(key_name='DB', sub_key_name='MSSQL',
                                                              sub_sub_key_name='TRUSTED_CONNECTION')

        print(
            'Driver=' + driver1 + 'Server=' + server1 + 'Database=' + database1 + 'Trusted_Connection=' + trusted_connection1)

        print(
            'Driver=' + driver2 + 'Server=' + server2 + 'Database=' + database2 + 'Trusted_Connection=' + trusted_connection2)

        # make connection string conn1 and connect to db1
        global conn1, conn2
        conn1 = pyodbc.connect(
            'Driver=' + driver1 + 'Server=' + server1 + 'Database=' + database1 + 'Trusted_Connection=' + trusted_connection1)

        # make connection string conn1 and connect to db2
        conn2 = pyodbc.connect(
            'Driver=' + driver2 + 'Server=' + server2 + 'Database=' + database2 + 'Trusted_Connection=' + trusted_connection2)

        conn_list = [conn1, conn2]

        return conn_list
        print("Connection to database successfull")

    def compare_tables(self, tables_frames):
        table_frame1 = tables_frames[0]
        table_frame2 = tables_frames[1]

        df1_new = table_frame1.merge(table_frame2, how='outer', indicator=True).loc[
            lambda x: x['_merge'] == 'left_only']
        df2_new = table_frame1.merge(table_frame2, how='outer', indicator=True).loc[
            lambda x: x['_merge'] == 'right_only']

        return [df1_new, df2_new]

    def execute_query(conn1, conn2, query1, query2):
        df1 = pd.read_sql(query1, conn1)
        df2 = pd.read_sql(query2, conn2)
        return [df1, df2]
