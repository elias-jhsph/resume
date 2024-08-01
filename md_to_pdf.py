import markdown
from weasyprint import HTML
import sys
import os

def convert_markdown_to_html(md_content):
    # Convert markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['extra', 'smarty'])

    # Define the HTML structure with improved styling and smaller margins
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @page {{
                margin: 0.5in 0.5in 0.5in 0.5in;  /* Set all margins to 0.5 inches */
            }}
            body {{
                font-family: Arial, sans-serif;
                margin: 0px;  /* Adjusted from 20px to 5px */
                padding: 5px; /* Adjusted from 20px to 5px */
                line-height: 1.4;
                font-size: 10px;
            }}
            h1 {{
                color: #333;
                font-size: 18px;
            }}
            h2 {{
                color: #333;
                font-size: 16px;
            }}
            h3 {{
                color: #333;
                font-size: 14px;
            }}
            h4 {{
                color: #333;
                font-size: 12px;
            }}
            h5 {{
                color: #333;
                font-size: 10px;
            }}
            h6 {{
                color: #333;
                font-size: 9px;
            }}
            p {{
                margin: 5px 0;
            }}
            ul, ol {{
                margin: 5px 0 5px 20px;
            }}
            li {{
                margin: 3px 0;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 1px 3px;
                border-radius: 3px;
            }}
            pre {{
                background-color: #f4f4f4;
                padding: 10px;
                border-radius: 3px;
                overflow-x: auto;
            }}
            blockquote {{
                border-left: 4px solid #ccc;
                margin: 5px 0;
                padding-left: 10px;
                color: #666;
            }}
            .section-title {{
                font-size: 12px;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 10px;
                border-bottom: 1px solid #ccc;
                padding-bottom: 3px;
            }}
            .contact-info {{
                margin-bottom: 20px;
            }}
            .contact-info p {{
                margin: 2px 0;
            }}
            .job-title {{
                font-size: 12px;
                font-weight: bold;
            }}
            .job-duration {{
                font-size: 10px;
                color: #666;
            }}
        </style>
        <title>Resume</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return html_template

def convert_markdown_file_to_pdf(md_file_path, output_pdf_path):
    try:
        # Load the Markdown file
        with open(md_file_path, 'r') as file:
            md_content = file.read()

        # Convert markdown to HTML with styling
        html_content = convert_markdown_to_html(md_content)

        # Save the HTML to a temporary file
        temp_html_path = 'temp_resume.html'
        with open(temp_html_path, 'w') as file:
            file.write(html_content)

        # Convert the HTML file to PDF
        HTML(temp_html_path).write_pdf(output_pdf_path)

        # Remove the temporary HTML file
        os.remove(temp_html_path)

        print(f'Successfully converted {md_file_path} to {output_pdf_path}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python convert_resume.py <input_markdown_file> <output_pdf_file>')
    else:
        md_file_path = sys.argv[1]
        output_pdf_path = sys.argv[2]
        convert_markdown_file_to_pdf(md_file_path, output_pdf_path)
