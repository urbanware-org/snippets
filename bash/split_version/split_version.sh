# Split version string into seperate numbers
version=$(foobar --version | sed -e "s/\./\ /g")
version_major=$(awk '{ print $1 }' <<< $version)
version_minor=$(awk '{ print $2 }' <<< $version)
version_revis=$(awk '{ print $3 }' <<< $version)
