# wheres-the-changelog

Find the changelog for a package using the online form: https://shangxiao.github.io/wheres-the-changelog/

### Why does this exist when repositories link to the changelog?

 - Not all package authors supply the changelog link
 - This can be used to programmatically open a changelog


Add this to your shell rc:

```sh
function changelog() {
    python -m webbrowser https://shangxiao.github.io/wheres-the-changelog/$1/$2
}
```

Then open a changelog:

```sh
changelog pypi django
```
