# Python Visual

Interactive visualization of the most-starred Python repositories on GitHub.

## Description

This project fetches live repository data from the GitHub Search API and presents it as an interactive Plotly bar chart. It is designed for anyone learning how to combine API requests, JSON data processing, and Python-based visualization in a simple, practical project.

The script focuses on Python repositories, sorts them by star count, and generates an HTML chart that can be opened in a web browser.

## Features

- Fetches repository data from the GitHub API
- Filters results to Python repositories sorted by stars
- Builds an interactive Plotly bar chart
- Displays repository owner and description on hover
- Creates clickable repository names in the chart
- Exports the final visualization as `python_repos.html`

## Technologies

- Python 3
- `requests`
- `plotly`
- GitHub REST API

## Installation

### Clone the repository

```bash
git clone <your-repository-link>
cd <your-repository-folder>
```

### Install dependencies

```bash
pip install requests plotly
```

## Usage

Run the script from inside the `python visual` folder:

```bash
python python_repos_visual.py
```

After running the script:

- GitHub repository data is fetched
- the chart is built from the returned data
- `python_repos.html` is generated

Open `python_repos.html` in your browser to view the interactive result.

## Project Structure

```text
python visual/
|-- python_repos_visual.py
`-- README.md
```

Generated output:

```text
python_repos.html
```

## How It Works

1. The script sends a request to the GitHub Search API.
2. It reads the returned JSON response.
3. It extracts repository names, links, star counts, owners, and descriptions.
4. It creates a Plotly bar chart from that data.
5. It saves the visualization as `python_repos.html`.

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

Add your preferred license here, such as MIT.

## Contact

Add your GitHub profile or email here if you want to include contact details.
