"""Database comparison feature tests."""
import pandas as pd
from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

from tests.pageobjects.db_comparison import DBComparison as db

scenarios('../features/db.feature')


@given(parsers.parse('connection is established between source and target databases'))
def connection_is_established_between_source_and_target_databases():
    """connection is established between source and target databases."""
    global conn
    conn = db.connect_to_dbs()


@when(parsers.parse('user executes "<query1>" on source and "<query2>" on target databases'))
def user_executes_query_on_source_and_on_target_databases(query1, query2):
    """user executes "<query1>" on source and "<query2>" on target databases."""
    conn1 = conn[0]
    conn2 = conn[1]
    global df
    df = db.execute_query(conn1, conn2, query1, query2)


@when(parsers.parse('results from both database resultsets are compared'))
def results_from_both_database_resultsets_are_compared():
    """results from both database resultsets are compared."""
    df1 = df[0]
    df2 = df[1]

    global df_new1, df_new2, df_final
    df_new1 = df1.merge(df2, how='outer', indicator=True).loc[lambda x: x['_merge'] == 'left_only']
    df_new2 = df1.merge(df2, how='outer', indicator=True).loc[lambda x: x['_merge'] == 'right_only']

    df_final = pd.concat([df_new1, df_new2])


@then(parsers.parse('user reports any mismatches'))
def user_reports_any_mismatches():
    """user reports any mismatches."""

    df_final.to_excel('././results/mismatches.xlsx')

