def create_well_metadata_table(connection):
    try:
        cur = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS well_metadata (
        well_id VARCHAR(255),
        well_status VARCHAR(255),
        well_type VARCHAR(255),
        well_owner VARCHAR(255),
        driller VARCHAR(255),
        primary_use VARCHAR(255),
        secondary_use VARCHAR(255),
        latitude DOUBLE PRECISION NOT NULL,
        longitude DOUBLE PRECISION NOT NULL,
        ecan_well_link VARCHAR(255),
        address_one VARCHAR(255),
        address_two VARCHAR(255),
        PRIMARY KEY (well_id)
        )
        """ 

        cur.execute(create_table_query)
        connection.commit()
        cur.close()
        print("Table Well Metadata created successfully")
    except Exception as e:
        print(f"ERROR: unable to create table {e}")
