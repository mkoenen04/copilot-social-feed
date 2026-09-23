# Social Media Feed

A simple Python console application that simulates a social media feed. Users can create posts, view the feed, like posts, and delete posts through an interactive text-based menu.

## Technologies Used

- **Python 3**
- Python standard library only
- In-memory list and dictionaries for post storage

## Installation and Setup

### Prerequisites

- Python 3.8 or newer

### Setup

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Confirm that Python is installed:

	```bash
	python --version
	```

4. No additional packages or dependencies are required.

## Usage

Start the application from the project directory with:

```bash
python main.py
```

Use the numbered menu to choose an action:

1. **View the feed** - Display all posts, including each author's name, post text, and current like count.
2. **Add a new post** - Enter an author and post message. New posts start with zero likes.
3. **Like a post** - Select a post by its number to increase its like count by one.
4. **Delete a post** - Select a post by its number to remove it from the feed.
5. **Exit** - Close the application.

### Example

```text
=== Social Media Feed ===
1. View the feed
2. Add a new post
3. Like a post
4. Delete a post
5. Exit
Choose an option: 2
Author: Alex
Post text: Welcome to my feed!
Post added!
```

Posts are stored in memory and are cleared when the program exits. The application also validates empty post details, invalid menu choices, and invalid post numbers.

## Features

- Interactive command-line menu
- View all posts in numbered order
- Add posts with an author and text
- Track likes for each post
- Delete posts by number
- Input validation with clear feedback messages
- No external dependencies

## Project Structure

```text
.
├── main.py      # Application source code
└── README.md    # Project documentation
```
