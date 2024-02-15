# wheres-the-changelog

Find the changelog for a package using the online form: https://shangxiao.github.io/wheres-the-changelog/

<p align="center"><img src="./wheres-the-changelog.png"  alt="where's the cheese?" height="400" /></p>

### Why does this exist when repositories link to the changelog?

 - Not all package authors supply the changelog link
 - This can be used to programmatically open a changelog


Add this to your shell rc:

```sh
function changelog() {
    if [ $# -lt 2 ]
    then
        echo 'Usage: changelog <repository> <package>'
    else
        for arg in "${@:2}"
        do
            python -m webbrowser https://shangxiao.github.io/wheres-the-changelog/$1/$arg
        done
    fi
}
```

Then open changelogs for multiple packages at a time:

```sh
changelog pypi django pytest pytest-django
```
