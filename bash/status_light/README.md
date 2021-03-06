# status_light

Methods to print the current status of an action e.g. with multiple steps using a circle that changes its color.

#### Sample output

<img src="https://raw.githubusercontent.com/urbanware-org/snippets/master/bash/status_light/status_light.gif" alt="Busy char sample output">

## Usage

### Code

The sample output was created using the following code.

```bash
status_msg "Reading file #1" "90m"
linecount_foobar1=$(wc -l /tmp/foobar1.txt)
status_done "92m"

status_msg "Reading file #2" "90m"
linecount_foobar2=$(wc -l /tmp/foobar2.txt)
status_done "92m"

status_msg "Reading file #3" "90m"
linecount_foobar3=$(wc -l /tmp/foobar3.txt)
status_done "92m"
```

### Color codes

| Color name    | Code          | Color name    | Code          |
| ------------- | ------------- | ------------- | ------------- |
| Black         | `30m`         | Dark gray     | `90m`         |
| Dark red      | `31m`         | Light red     | `91m`         |
| Dark green    | `32m`         | Light green   | `92m`         |
| Brown         | `33m`         | Yellow        | `93m`         |
| Dark blue     | `34m`         | Light blue    | `94m`         |
| Dark purple   | `35m`         | Light purple  | `95m`         |
| Dark cyan     | `36m`         | Light cyan    | `96m`         |
| Light gray    | `37m`         | White         | `97m`         |
