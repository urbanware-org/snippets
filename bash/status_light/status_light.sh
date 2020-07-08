status_msg() {
    message=$1
    color_code=$2
    echo -e "  \r\e[${color_code}•\e[0m $message\c"
}

status_done() {
    color_code=$1
    echo -e "\r\e[${color_code}•\e[0m"
}
