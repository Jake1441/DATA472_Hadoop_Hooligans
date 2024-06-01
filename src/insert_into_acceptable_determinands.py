import pandas as pd


def insert_into_acceptable_determinands(connection, row):
    try:
        cur = connection.cursor()
        insert_into_command = """
        INSERT INTO acceptable_determinands_v2
        (
            chloride,
            hardness_total,
            calcium,
            ph,
            ph_field,
            sodium_dissolved,
            sulphate,
            water_temperature,
            oxygen_dissolved,
            magnesium,
            silica,
            nitrate_nitrogen,
            e_coli,
            total_coliforms
        )
        VALUES
        (
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s,
         %s
        );
        """
        cur.execute(
            insert_into_command,
            (
                row["Well_No"],
                row["Well_Status"],
                row["Well_Type"],
                row["Well_Owner"],
                row["Driller"],
                row["Primary_Use"],
                row["Secondary_Use"],
                row["WGS84_LATITUDE"],
                row["WGS84_LONGITUDE"],
                row["Link"],
                row["Locality"],
                row["Street"],
            ),
        )
        connection.commit()
        print("Data Inserted")
        cur.close()
    except Exception as e:
        print(f"Exception occured at {row['Well_No']} {e}")
