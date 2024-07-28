# parsingBankruptcy
collecting data from the site  https://old.bankrot.fedresurs.ru  and sending via telegram
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1, h2, h3 {
            color: #333;
        }

        pre {
            background: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }

        code {
            font-family: monospace;
            background: #f4f4f4;
            padding: 2px 4px;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Parsing and Saving Auction Data</h1>
        <p>This project provides a tool for scraping auction data from a specific website, processing it, and saving the results into a CSV file. The code uses Selenium and BeautifulSoup for web scraping and CSV for data storage.</p>

        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#functions">Functions</a>
                <ul>
                    <li><a href="#save_data">save_data</a></li>
                    <li><a href="#parsing_data">parsing_data</a></li>
                    <li><a href="#data_collection">data_collection</a></li>
                </ul>
            </li>
            <li><a href="#main-function">Main Function</a></li>
            <li><a href="#dependencies">Dependencies</a></li>
            <li><a href="#license">License</a></li>
        </ul>

        <h2 id="installation">Installation</h2>
        <ol>
            <li>
                <p><strong>Clone the repository:</strong></p>
                <pre><code>git clone https://github.com/yourusername/yourrepository.git
cd yourrepository</code></pre>
            </li>
            <li>
                <p><strong>Create and activate a virtual environment:</strong></p>
                <pre><code>python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`</code></pre>
            </li>
            <li>
                <p><strong>Install the required packages:</strong></p>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
        </ol>

        <h2 id="usage">Usage</h2>
        <p>To run the script and start the data collection process, simply execute the following command in your terminal:</p>
        <pre><code>python parsing.py</code></pre>
        <p>The script will scrape the data from the specified website and save it to a CSV file named <code>sw_data_new.csv</code>.</p>

        <h2 id="functions">Functions</h2>

        <h3 id="save_data">save_data</h3>
        <pre><code>def save_data(data: list) -> None:</code></pre>
        <p>This function saves the parsed data into a CSV file.</p>
        <ul>
            <li><strong>Parameters</strong>:
                <ul>
                    <li><code>data</code> (list): A list of lists containing the parsed data.</li>
                </ul>
            </li>
            <li><strong>Behavior</strong>:
                <ul>
                    <li>Creates or opens a CSV file named <code>sw_data_new.csv</code>.</li>
                    <li>Writes the header row and the data rows to the CSV file.</li>
                </ul>
            </li>
        </ul>

        <h3 id="parsing_data">parsing_data</h3>
        <pre><code>def parsing_data(driver: Chrome) -> list[list[str]]:</code></pre>
        <p>This function parses data from a webpage using a Selenium WebDriver.</p>
        <ul>
            <li><strong>Parameters</strong>:
                <ul>
                    <li><code>driver</code> (Chrome): A Selenium WebDriver instance for the Chrome browser.</li>
                </ul>
            </li>
            <li><strong>Returns</strong>:
                <ul>
                    <li><code>result</code> (list[list[str]]): A list of lists containing the parsed table data.</li>
                </ul>
            </li>
        </ul>

        <h3 id="data_collection">data_collection</h3>
        <pre><code>def data_collection(url: str) -> list[list[str]]:</code></pre>
        <p>This function controls the flow of the scraping process, handling pagination and data aggregation.</p>
        <ul>
            <li><strong>Parameters</strong>:
                <ul>
                    <li><code>url</code> (str): The URL of the webpage to scrape.</li>
                </ul>
            </li>
            <li><strong>Returns</strong>:
                <ul>
                    <li><code>data</code> (list[list[str]]): A list of lists containing all the scraped data.</li>
                </ul>
            </li>
        </ul>

        <h2 id="main-function">Main Function</h2>

        <h3>main</h3>
        <pre><code>def main() -> None:</code></pre>
        <p>The entry point of the script. This function initiates the data collection process and calls the <code>save_data</code> function to store the results.</p>

        <h2 id="dependencies">Dependencies</h2>
        <ul>
            <li><code>csv</code>: For writing data to CSV files.</li>
            <li><code>time</code>: For adding delays between page loads.</li>
            <li><code>bs4</code> (BeautifulSoup): For parsing HTML content.</li>
            <li><code>selenium</code>: For automating web browser interaction.</li>
        </ul>
        <p>To install the dependencies, run:</p>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h2 id="license">License</h2>
        <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
    </div>
</body>

</html>
