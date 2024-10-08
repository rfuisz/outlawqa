note -- to install the paper-qa submodule, run the following:
pip install -e "submodules/paper-qa[ldp,typing,zotero]"

to install the paper-scraper submodule, run the following:
pip install -e "submodules/paper-scraper"

to run outlawqa, simply run the following:

```bash
python3.12 outlawqa.py
```

or the usual set of pqa cli should work too if you set the paper directory to downloaded_papers -- see the paper-qa README for more details, but basically:

```bash
cd paper-qa
pqa ask "what is the best way to learn about the history of the internet?"
```

create a .env file with the following:

```bash
OPENAI_API_KEY=sk-proj-blank
DOI2PDF=https://blank
CROSSREF_MAILTO=blank@gmail.com
SERPAPI_API_KEY=blank

## optionally, if you want less rate limiting:
SEMANTIC_SCHOLAR_API_KEY=blank
CROSSREF_API_KEY=blank
```
