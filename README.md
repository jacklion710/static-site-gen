# Static Site Generator

This project is a static site generator built in Python. It allows for the generation of HTML pages from markdown files, providing a simple and flexible way to create and manage content. This project was guided by [boot.dev](http://boot.dev).

## Features

- **Recursive Page Generation**: Generates HTML pages for every markdown file found in a specified directory, maintaining the directory structure in the output.
- **Template-based Rendering**: Utilizes a single HTML template to render all pages, ensuring consistent design across the site.
- **Support for Markdown Features**: Converts common markdown syntax to HTML, including headings, paragraphs, bold/italic text, links, images, and code blocks.
- **Simple Static Server**: Includes a basic static file server for local testing and previewing of the generated site.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Optional: virtual environment

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/static-site-gen.git
    cd static-site-gen
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

### Usage

1. **Generating the Site**

    To generate the static site, run the `main.sh` script:

    ```bash
    bash main.sh
    ```

    This script executes the static site generator, processing all markdown files found in the `content` directory and outputting the generated HTML pages to the `public` directory.

2. **Running the Server**

    To preview your site locally, start the included static file server:

    ```bash
    python server.py --dir public
    ```

    By default, the server runs on `http://localhost:8888`. Open this URL in your web browser to view your site.

3. **Running Tests**

    To run the unit tests, execute the `test.sh` script:

    ```bash
    bash test.sh
    ```

    This runs all tests found in the `src` directory, ensuring the components of your static site generator are functioning correctly.

## Project Structure

- `content/`: Markdown files organized into directories.
- `public/`: Output directory for generated HTML pages and static assets.
- `src/`: Python source files for the static site generator and tests.
- `static/`: Static assets such as CSS, images, and JavaScript.
- `template.html`: HTML template used for rendering pages.
- `main.sh`: Script to generate the static site.
- `test.sh`: Script to run unit tests.
- `server.py`: Simple static file server for local testing.