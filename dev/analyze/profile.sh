#!/bin/bash

cur_date=$(date +%s%N | cut -b1-13)
cur_dir=$(pwd)
nginx_temp="/tmp/$cur_date-nginx.log"

file_bu="$cur_dir/profile-results/$cur_date-bu.csv"
nginx_bu="$cur_dir/profile-results/$cur_date-bu-nginx.log"
tree_file_bu="$cur_dir/profile-results/$cur_date-bu-nginx-tree.log"
stats_file_bu="$cur_dir/profile-results/$cur_date-bu-nginx-stats.csv"

file_gui="$cur_dir/profile-results/$cur_date-gui.csv"
nginx_gui="$cur_dir/profile-results/$cur_date-gui-nginx.log"
tree_file_gui="$cur_dir/profile-results/$cur_date-gui-nginx-tree.log"
stats_file_gui="$cur_dir/profile-results/$cur_date-gui-nginx-stats.csv"


cd tests
source venv/bin/activate

# Run BU tests
echo "TS,PID,Process,CLKS,CLK_TCK,Command" > $file_bu
$cur_dir/stat.sh $file_bu
pytest test_bu_insertion.py
$cur_dir/stat.sh $file_bu
sleep 1
docker exec -it dev-nginx cat /var/log/nginx/redirect.log > $nginx_bu
bu_lines=$(cat $nginx_bu | wc -l)
bu_lines=$(($bu_lines +1))

# Run GUI tests
echo "TS,PID,Process,CLKS,CLK_TCK,Command" > $file_gui
$cur_dir/stat.sh $file_gui
pytest test_gui.py
$cur_dir/stat.sh $file_gui
sleep 1
docker exec -it dev-nginx cat /var/log/nginx/redirect.log > $nginx_temp
tail $nginx_temp -n +$bu_lines > $nginx_gui
deactivate

cd $cur_dir

# Parse nginx logs
cd analyzer

source venv/bin/activate
python analyze.py $nginx_bu  $tree_file_bu  $stats_file_bu
python analyze.py $nginx_gui $tree_file_gui $stats_file_gui
deactivate

cd $cur_dir