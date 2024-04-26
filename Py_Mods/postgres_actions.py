import requests

import Py_Mods.read_postgrest_conf as pg_conf

curl_token = pg_conf.open_pg_conf("pgrest_conf/test_curl_post.sh", "TOKEN")
url = 'http://localhost:3000/data'


def db_commit(db_data):
    """
    :type db_data: text/csv example
    first row = column names
    second row = data
    """
    # May require a target database
    print(db_data)
    print(type(db_data))

    headers = {
        'Authorization': f'Bearer {curl_token}',
        "Content-Type": "text/csv"
    }

    """ commit data to the actual database """
    r = requests.post(url,
                      headers=headers,
                      data=db_data  # from payload_data
                      )
    print(r.status_code)
