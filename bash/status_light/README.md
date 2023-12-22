# status_light

Functions to print the current status of an action e.g. with multiple steps using a circle that changes its color.

For example:

<img src="https://raw.githubusercontent.com/urbanware-org/snippets/master/bash/status_light/status_light.gif" alt="Busy char sample example">

## Usage

### Code

#### Sample output

The sample output was created using the following code.

```bash
status_msg "Reading file #1" "90m"
linecount_file1=$(wc -l /tmp/foobar1.txt)
status_done "92m"

status_msg "Reading file #2" "90m"
linecount_file2=$(wc -l /tmp/foobar2.txt)
status_done "92m"

status_msg "Reading file #3" "90m"
linecount_file3=$(wc -l /tmp/foobar3.txt)
status_done "92m"
```

#### Conditions

Of course, the function `status_done` can be used not only as a progress indicator but also as a status.

For example:

```bash
file="/tmp/foobar.txt"
status_msg "Reading file '$file'" "90m"
if [ ! -f "$file" ]; then
    status_done "91m"   # given path does either not exist or is not a file,
                        # so print a red circle
else # file exists
    linecount=$(wc -l "$file")
    if [ $linecount -lt 1 ]; then
        status_done "93m"   # file is empty, print a yellow circle
    else
        status_done "92m"   # file is not empty, print a green circle
    fi
fi
```

### Color codes

| Color name    | Code          |   | Color name    | Code          |
| ------------- | ------------- | - | ------------- | ------------- |
| Black         | `30m`         |   | Dark gray     | `90m`         |
| Dark red      | `31m`         |   | Light red     | `91m`         |
| Dark green    | `32m`         |   | Light green   | `92m`         |
| Brown         | `33m`         |   | Yellow        | `93m`         |
| Dark blue     | `34m`         |   | Light blue    | `94m`         |
| Dark purple   | `35m`         |   | Light purple  | `95m`         |
| Dark cyan     | `36m`         |   | Light cyan    | `96m`         |
| Light gray    | `37m`         |   | White         | `97m`         |
