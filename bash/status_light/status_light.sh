status_msg() {
    message=$1
    color_code=$2
    echo -e "  \r\e[${color_code}•\e[0m $message\c"
}

status_done() {
    color_code=$1
    echo -e "\r\e[${color_code}•\e[0m"
}

status_msg "Reading file #1" "90m"
sleep 3
status_done "92m"
status_msg "Reading file #2" "90m"
sleep 3
status_done "92m"
status_msg "Reading file #3" "90m"
sleep 3
status_done "92m"
