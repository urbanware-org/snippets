# split_version

Simple code to split version string into seperate numbers.

## Usage

For example, if the `foobar` tool returns the following version string

```
$ foobar --version
3.2.6
$
```

the `split_version` snippet can separate it into the **major**, **minor** and **revision** number:

```bash
version=$(foobar --version | sed -e "s/\./\ /g")
version_major=$(awk '{ print $1 }' <<< $version)
version_minor=$(awk '{ print $2 }' <<< $version)
version_revis=$(awk '{ print $3 }' <<< $version)
```

in order to simplify version comparisons.
