# JURRI's new website 2019

The template is downloaded from Wrappixel.

[Click here to check the original template](https://wrappixel.com/demos/ui-kit/wrapkit-free/wrapkit/index.html)

## Development instructions

### Make changes to the Website

1. Ask permission to become collaborator in the git repository.

1. Clone repository to your own PC and do changes that are needed.

1. Commit your changes and push them to git.

1. Connect the server by using SSH. The instructions are found from our google drive.

1. On the server, change directory and update website changes by

```bash
cd public_html/
git pull
```

and then the website is updated.

### Update date in the footer

To update the dates on the pages, you need to modify the
dates to all .html files. There is a script for updating
the dates in all .html files. Update all dates by running

```bash
python update_date.py
```
