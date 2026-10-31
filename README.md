# Sohel Georgiadis

A static personal website with eight papers, acknowledgements, and a reading list.

## Website

The publishing entry point is `index.html` at the root of this folder. The site
uses relative links and includes its HTML, CSS, JavaScript, images, and PDFs.
There is no application server or build step required to publish it.

For GitHub Pages, push this folder's contents to a repository and select that
branch's root as the publishing source. The `.nojekyll` file keeps it a plain
static site. See [GitHub's publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

To preview locally, run `python3 -m http.server` from this directory, or open
`index.html` directly in a browser.

## Papers

The finished PDFs are in `papers/`. Editable LaTeX sources are in `source/papers/`.
Seven manuscripts embed their image and class dependencies. The historical
paper keeps its figures in the adjacent `figures/` folder to retain the full
images. Its project must be compiled with that folder present.

With Tectonic installed, run `python3 source/build_papers.py` to rebuild the
PDFs. This step is optional and is separate from publishing the website.

## Attribution

Asset credits and the archived interface provenance are recorded in
`THIRD_PARTY_NOTICES.txt` and in the papers. Third-party assets retain their
respective rights; this repository does not apply a blanket licence to them.
