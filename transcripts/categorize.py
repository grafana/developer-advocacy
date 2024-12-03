import sys, csv, requests
from bs4 import BeautifulSoup
import markdownify
import trafilatura
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

def read_urls(file_path='rest.csv'):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.
    Each dictionary represents a row, with column headers as keys.

    :param file_path: Path to the CSV file. Defaults to 'urls.csv'.
    :return: List of rows as dictionaries.
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]
        return rows
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def fetch_url_to_markdown(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        # Extract the main content using trafilatura
        main_content = trafilatura.extract(html_content, include_formatting=True, include_links=True)

        if not main_content:
            return "Could not extract main content from the page. It might be heavily structured or unsupported."

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the visible text
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()  # Remove JavaScript and CSS

        # Get the main content
        text_content = soup.get_text(separator='\n')

        # Convert to Markdown using markdownify
        markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")

        return markdown_content
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
    except Exception as e:
        return f"Error processing the content: {e}"

# Example usage
if __name__ == "__main__":
    urls = read_urls()
    print(urls)

    client = OpenAI()

    fp = open("results.csv", mode='w', newline='', encoding='utf-8')
    writer = csv.DictWriter(fp, fieldnames=['page_title', 'page_url', 'summary', 'productTags', 'topicTags', 'materialTags', 'extraTags', '# orgs viewed (in my scope) '])
    writer.writeheader()

    # url = input("Enter the URL: ")
    url = 'https://grafana.com/docs/grafana/latest/datasources/'

    for idx, entry in enumerate(urls):
        url = entry['page_url']
        print(url)
        markdown = fetch_url_to_markdown(url)

        print("URL %d: %s" % (idx, url))
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful summarizer who will assist in describing what pages are about, and categorizing them. " +
                        "All of the pages are about Grafana Labs software."
                    )
                },
                {
                    "role": "system",
                    "content": (
                        "Please read the entire document, and summarize the main body from the perspective of what " +
                        "it would help a user accomplish with Grafana's software. Please pick no more than 3 or 4 tags" +
                        "to describe it. I will provide some example tags you can choose from, but you can come up with others " +
                        "if none of the provided options seem to fit.  Here are some sample tags: " +
                        "Product tags indicate what product the page describes: Grafana, Loki, Mimir, Tempo, K6, Faro, Beyla, Alloy, Agent " +
                        "Topic tags describe what facet of the product the page describes: installation, configuration, data-sources, plugins, dashboards, security, pricing, architecture, etc. " +
                        "Material tags indicate what kind of technical content it is: Overview, Summary, Tutorial, Reference, Troubleshooting, General, etc. " +
                        "Extra tags indicate other technologies or integrations the page may describe or involve: Beta, OpenTelemetry, Prometheus, Azure, Google Cloud, AWS, Graphite, etc. " +
                        "A good set of tags will be a single product tag, one or more topic tags, ONLY ONE material tag, and (only if applicable) an extra tag. " +
                        "Assign only one product tag that is the main focus of the page. Many products may be identified two ways, such as Beyla and Grafana Beyla. " +
                        "in those cases, use the shorter name.  For example, use Beyla instead of Grafana Beyla. " +
                        "Assign only one material tag that best describes the primary type of content. " +
                        "For topic tags, you may assign up to 3.  If you are unsure, you may assign only one. " +
                        "You may assign up to 3 extra tags. " + 
                        "This is not a complete list of product, topic, and focus tags, you may create new ones, but " +
                        "if an existing tag fits, please use it.  The name of any third-party technology, database, or product is an acceptable "+
                        "extra tag, such as InfluxDB, MySQL, Postgres, DataDog, etc, but do not use these as topic tags."
                    )
                },
                { 
                    "role": "system", 
                    "content": (
                        "Output one json object with the following keys: summary, productTags, topicTags, materialTags, extraTags.  Each tags field must be an array of strings"
                    )
                },
                { "role": "user", "content": markdown }
            ],
            model="gpt-4o",
            response_format={"type": "json_object"},
        )

        obj = json.loads(completion.choices[0].message.content)
        # print(obj)
        entry['summary'] = obj['summary']

        for key in ['productTags', 'topicTags', 'materialTags', 'extraTags']:
            entry[key] = ','.join([x.lower() for x in obj[key]])

        writer.writerows([entry])
        fp.flush()
    
    print("Finished")
    fp.close()
    # Response format (poorly documented)
    # ChatCompletion(id='chatcmpl-AVm4xzmSv21BjCWblYoq6jLnAXzYI', 
    # choices=[Choice(finish_reason='stop', index=0, logprobs=None, 
    # message=ChatCompletionMessage(content="Why don't skeletons fight each other?\n\nThey don't have the guts.", 
    # refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], 
    # created=1732136347, model='gpt-4o-2024-08-06', object='chat.completion', 
    # service_tier=None, system_fingerprint='fp_45cf54deae', 
    # usage=CompletionUsage(completion_tokens=14, prompt_tokens=11, total_tokens=25, 
    # completion_tokens_details=CompletionTokensDetails(
    # accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), 
    # prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
    # print(completion.choices[0].message.content)
