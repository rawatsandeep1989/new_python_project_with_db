#!/usr/bin/env python3

import argparse
import json
import sys
import db

def config_file():
#    This file is just another way to define a constant which will be returned when we call this function
    return "/home/sandeepr/new_python_project_with_db/config/db_config"


def main():
    try:
        with open(config_file(), "r") as file:
            #Code here
      #      print("yahoo file opened successfully")
            db_details = json.load(file)
      #      print(db_details['_comment'])
            hostname=db_details['database_details']['hostname']
            username=db_details['database_details']['username']
            password=db_details['database_details']['password']
            database=db_details['database_details']['db']
            db_connect_obj = db.db_connect(hostname,username,password,database) 
            print("Connected successfully")



    except IOError as e: 
            print("IO Error : {error}".format(error=e))

if __name__ == "__main__":
    main()
