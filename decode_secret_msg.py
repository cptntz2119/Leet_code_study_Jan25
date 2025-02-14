import requests

def fetch_google_doc(url):
    """
    Fetches the text content from a Google Doc URL.
    The document must be shared as "Anyone with the link can view".
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("✅ Successfully fetched data!")
        raise Exception(f"Error fetching document: {response.status_code}")
    else:
         print(f"❌ Failed to fetch data. HTTP Status Code: {response.status_code}")
    return response.text  # Assuming the doc is in raw text format

def parse_data(doc_text):
    """
    Parses the document text to extract Unicode characters and their (x, y) positions.
    Returns a list of (char, x, y) tuples.
    """
    data_points = []
    
    for line in doc_text.strip().split("\n"):
        parts = line.split()
        if len(parts) != 3:
            continue  # Ignore invalid lines
        
        char = parts[0]   # Unicode character
        try:
            x = int(parts[1])  # X-coordinate
            y = int(parts[2])  # Y-coordinate
            data_points.append((char, x, y))
        except ValueError:
            continue  # Ignore lines with invalid numbers
    
    return data_points

def build_grid(data_points):
    """
    Constructs a 2D grid based on the extracted data points.
    """
    if not data_points:
        return []

    # Find max x and y values to determine grid size
    max_x = max(point[1] for point in data_points)
    max_y = max(point[2] for point in data_points)

    # Create a grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with characters at their respective positions
    for char, x, y in data_points:
        grid[y][x] = char  # Place character at correct position

    return grid

def print_grid(grid):
    """
    Prints the grid to display the message.
    """
    for row in grid:
        print("".join(row))

def display_google_doc_message(url):
    """
    Main function: Fetches data, parses it, builds the grid, and prints the message.
    """
    # Step 1: Fetch document text
    doc_text = fetch_google_doc(url)

    # Step 2: Parse the extracted text into structured data
    data_points = parse_data(doc_text)

    # Step 3: Construct the character grid
    grid = build_grid(data_points)

    # Step 4: Print the resulting grid
    print_grid(grid)

# Example usage:
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
display_google_doc_message(url)
