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
            url=https://shangxiao.github.io/wheres-the-changelog/$1/$arg
            response=$(curl --write-out '%{http_code}' --head --silent --output /dev/null $url)
            if [ $response -eq '404' ] ; then
                # Open a PR instead if the page doesn't exist yet
                filename=$arg.html
                # encoded version of <meta http-equiv="refresh" content="0;URL='???'" />
                value="%3Cmeta+http-equiv%3D%22refresh%22+content%3D%220%3BURL%3D%27%3F%3F%3F%27%22+%2F%3E"
                url="https://github.com/shangxiao/wheres-the-changelog/new/main/$1?filename=$filename&value=$value"
            fi
            # or simpley `open $url` on a Mac
            python -m webbrowser $url
        done
    fi
}
```

Then open changelogs for multiple packages at a time:

```sh
changelog pypi django pytest pytest-django
```
