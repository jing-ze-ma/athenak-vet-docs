# AthenaK VET radiation documentation

User documentation for the clean VET radiation scheme of
[AthenaK](https://github.com/jing-ze-ma/athenak) (branch `vet-clean-release`), built with
[Sphinx](https://www.sphinx-doc.org/) and the [Furo](https://pradyunsg.me/furo/) theme.
Worked problems with notebooks are in
[athenak-vet-gallery](https://github.com/jing-ze-ma/athenak-vet-gallery).

The layout, theme, style sheet and workflow are those of the
[IAS AthenaK documentation](https://github.com/IAS-Astrophysics/athenak-docs); we thank its authors.

The published site is hosted on GitHub Pages:
<https://jing-ze-ma.github.io/athenak-vet-docs/>.

## Building locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

sphinx-build -b html source build/html
```

Then open `build/html/index.html` in a browser. Alternatively, use `make html`.

## Where the text comes from

The text of the scheme lives with the code, in `docs/vet_clean/*.md` and
`tests/vet_clean/README.md` of the code repository, and is updated in the same commit as the
code. `tools/sync_from_code.py` converts it (pandoc) and splits it into the pages of this
site; those pages start with a "generated" comment. After a change in the code repository:

```bash
pip install -r tools/requirements-sync.txt
python tools/sync_from_code.py /path/to/athenak     # a checkout of the release
sphinx-build -W --keep-going -b html source build/html
```

`index.rst`, `gallery.rst` and `faq.rst` are written by hand.

## Continuous integration

The [`Docs` workflow](.github/workflows/docs.yml) runs on every push and pull request:

- **Build (strict)**: builds the site with `sphinx-build -W --keep-going`, so any
  Sphinx warning fails the check and broken docs cannot be merged.
- **Deploy**: on `main`, the built site is published to GitHub Pages.
