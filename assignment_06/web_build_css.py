import os # Interacting with the operating system. Can create directories, handle file paths, manage file system
import re # Allows me to work with regular expressions. Matching, searching, and maniupulating strings. 

# Slugify function.
def slugify(title): # regular expression
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html'
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"

# Nav function.
def generate_nav(titles, active_title): # regular expression
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    for title in titles: # Example of a for loop to iterate over titles
        filename = slugify(title)
        active_class = ' class="active"' if title == active_title else "" # Example of an if statement
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n' # Example of using an f-string
    return nav_links.strip()

# Create html function.
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)
    nav = generate_nav(titles, active_title=title)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # Coding for a directory to be created

    with open(output_path, 'w') as file:
        file.write(html_content) # writes content to file 

    print(f"Created {filename} in the '{output_dir}' directory.")

 # Create CSS file function
def create_css_file(output_dir="build"): # this is an example of a method 
    """Generate and write the style.css file based on a dictionary of styles.""" # this is a dictionary 
    styles = {
        "font-family": "Calibri",             # font family
        "body-background": "#7BAFD4",     # Background color for .content
        "nav-background": "#13294B",          # Background color for nav
        "nav-a-color": "#4B9CD3",              # Text color for nav links
        "nav-a-active-color": "#ffffff"
    }

    css_content = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """

    css_path = os.path.join(output_dir, "style.css")
    with open(css_path, 'w') as file: # Example of using with open() as file
        file.write(css_content) # Example of file.write

    print(f"Created style.css in the '{output_dir}' directory.")



def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Me", "My Experience", "My Projects"]

    # Create HTML files for each title
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file
        create_css_file() 
    

# if len(titles)==0 
    # pass . another example of using the pass statement that was on the web_build code 

if __name__ == "__main__":
    main() # Method call to start the program 