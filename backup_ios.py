from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg
import tftpy
from typing import Optional
import typer
import getpass
import os

def main(upload: Optional[str] = None):

    user = ""
    while user == "":
        user = input("Enter username: ")

    passwd = ""
    while passwd == "":
        passwd = getpass.getpass("Enter password: ")

    with open("devices.txt", "r") as f:
        device_list = f.read().splitlines()

    try:
        os.mkdir("configs")
    except:
        print("Error creating './configs' directory, it may already exist.")


    for d in device_list:
        DEVICE = {
            "host": d,
            "auth_username": user,
            "auth_password": passwd,
            "auth_strict_key": False,
            "transport_options": {
                "open_cmd": ["-o", "KexAlgorithms=+diffie-hellman-group14-sha1"]
            },
            "platform": "cisco_iosxe",
        }


        # open the "normal" scrapli connection
        with Scrapli(**DEVICE) as conn:
            # create the scrapli cfg object, passing in the scrapli connection, we are also using the
            # scrapli_cfg factory, so we can just pass the connection object and it will automatically
            # find and return the IOSXE (in this case) scrapli-cfg object
            cfg_conn = ScrapliCfg(conn=conn)

            # load up the new candidate config, set replace to True
        
            cfg_conn.prepare()
            my_config = cfg_conn.get_config().result
            print(f"Backing up config for {d}.")

            with open(f"./configs/{d}.txt", "w+") as f:
                f.write(my_config)

            if upload:
                client = tftpy.TftpClient(upload, 69)
                client.upload(f"{d}.txt", f"configs/{d}.txt")
                print(f"Config uploaded to {upload}.")


    print("All done, bye.") 



if __name__ == "__main__":
    typer.run(main)


