# This is a simple example that does not make any sense actually, just to show
# how you can tell the user that the system/process seems to be alive. In case
# you are a sadistic bastard, you may set an infinite loop in combination with
# a delay. None of my business at all.

# You can also use other characters (such as Unicode characters) instead of a
# spinning bar. For details see the 'CHAR_EXAMPLES' file.
bc_charset='/-\|'
bc_current=0

# This loop simply reads the file given below line by line and after each of
# them, the dash continues to rotate. When done, the number of read lines will
# be returned.
input_file="/var/log/syslog"

# The first of the following code blocks uses 'sleep' for a delay, which is
# absolutely unnecessary and was only added to make the dash animation easier
# to view.

line_count=0
while read line; do
    printf "Reading file. Please wait. ${bc_charset:$bc_current:1} \r"
    bc_current=$(( (bc_current + 1) % 4 ))
    line_count=$(( line_count + 1 ))
    sleep 0.06
done < $input_file
printf "Done. Processed $line_count lines.           \n"

# You can also add the progress in percent as shown in the example below.

percent=0
line_count=0
lines_total=$(wc -l < $input_file)
echo "Reading file. Please wait."
while read line; do
    printf "Progress: $percent %% ${bc_charset:$bc_current:1} \r"
    bc_current=$(( (bc_current + 1) % 4 ))
    line_count=$(( line_count + 1 ))
    percent=$(printf '%3s' $(bc <<< "($line_count * 100) / $lines_total"))
done < $input_file
printf "Done. Processed $line_count lines.\n"
