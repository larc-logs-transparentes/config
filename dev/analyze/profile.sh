#!/bin/bash

cur_date=$(date +%s%N | cut -b1-13)
file="profile-results/$cur_date.csv"
logs="profile-results/$cur_date.log"
nginx="profile-results/$cur_date-nginx.log"
tree_file="profile-results/$cur_date-nginx-tree.log"
stats_file="profile-results/$cur_date-nginx-stats.csv"

cur_dir=$(pwd)

# Run tests
cd tests
source venv/bin/activate

echo "TS,PID,Process,CLKS,CLK_TCK,Command" > $cur_dir/$file
$cur_dir/stat.sh $cur_dir/$file

pytest test_bu_insertion.py

$cur_dir/stat.sh $cur_dir/$file

deactivate

cd $cur_dir

# Get logs
docker compose logs | grep TLOG | tr -s " " | cut -f 3- -d ' ' > $logs
docker exec -it dev-nginx cat /var/log/nginx/redirect.log > $nginx

# Parse nginx logs
cd analyzer

source venv/bin/activate
python analyze.py ../$nginx ../$tree_file ../$stats_file
deactivate

cd $cur_dir