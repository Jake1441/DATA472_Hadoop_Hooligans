# this file reads the postgrest configuration

def open_pg_conf(file_name, key_name, starting_line="export"):
    """
    Open a configuration file by its name and search for the key name and extract the secret.

    :param key_name: name of key to look for.
    :param file_name: File name the secret is in
    :param starting_line: If starting line is specific look for this line.
    :return:
    """
    with open(file_name, mode='r') as file:
        """
        Open file, look for export command 
        """
        for line in file:
            if line.startswith(starting_line) and line.__contains__(key_name):
                return line.split('"')[1]
