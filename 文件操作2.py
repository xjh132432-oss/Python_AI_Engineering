import json
import os
count=0
def load_data():
    if os.path.exists("count.txt"):
        with open("count.txt","r",encoding="utf-8") as f:
            return
