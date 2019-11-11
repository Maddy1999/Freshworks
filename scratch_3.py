import os
import json
import sys
from collections import defaultdict
folder_path = input()
ip_base_name = input()
op_base_name = input()
max_fsize = int(input())
for x in os.listdir(folder_path):
    if x.endswith("json") and x.startswith(op_base_name):
        merge_file = x
txt_files = [x for x in os.listdir(folder_path) if x.endswith("json") and x.startswith(ip_base_name)]
merge_dict = defaultdict(list)
for i in range(len(txt_files)):
    with open(folder_path+'\\'+txt_files[i]) as f1:
        first_list = json.load(f1)
        for key, value in first_list.items():
            merge_dict[key].append(value)
print(json.dumps(merge_dict,indent=1))
print(sys.getsizeof(merge_dict))
if sys.getsizeof(merge_dict) < max_fsize:
    with open(folder_path+'\\'+merge_file,'w') as json_file:
        json.dump(merge_dict, json_file)



