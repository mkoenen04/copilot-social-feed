"""A simple console-based social media feed."""


# Each post is stored as a dictionary with an author, text, and like count.
posts = []


def view_feed():
	"""Display all posts in the feed."""
	if not posts:
		print("\nThe feed is empty.\n")
		return

	print("\n--- Social Feed ---")
	for number, post in enumerate(posts, start=1):
		print(f"{number}. {post['author']}: {post['text']}")
		print(f"   Likes: {post['likes']}")
	print()


def add_post():
	"""Ask the user for post details and add the post to the feed."""
	print("\n--- Add a New Post ---")
	author = input("Author: ").strip()
	text = input("Post text: ").strip()

	if not author or not text:
		print("Author and post text cannot be empty.\n")
		return

	posts.append({"author": author, "text": text, "likes": 0})
	print("Post added!\n")


def like_post():
	"""Add one like to a post selected by the user."""
	if not posts:
		print("\nThere are no posts to like.\n")
		return

	view_feed()
	choice = input("Enter the post number to like: ").strip()

	try:
		post_number = int(choice)
	except ValueError:
		print("Please enter a valid number.\n")
		return

	if 1 <= post_number <= len(posts):
		posts[post_number - 1]["likes"] += 1
		print("Post liked!\n")
	else:
		print("That post number does not exist.\n")


def delete_post():
	"""Delete a post selected by the user."""
	if not posts:
		print("\nThere are no posts to delete.\n")
		return

	view_feed()
	choice = input("Enter the post number to delete: ").strip()

	try:
		post_number = int(choice)
	except ValueError:
		print("Please enter a valid number.\n")
		return

	if 1 <= post_number <= len(posts):
		posts.pop(post_number - 1)
		print("Post deleted!\n")
	else:
		print("That post number does not exist.\n")


def main():
	"""Run the main menu until the user chooses to exit."""
	while True:
		print("=== Social Media Feed ===")
		print("1. View the feed")
		print("2. Add a new post")
		print("3. Like a post")
		print("4. Delete a post")
		print("5. Exit")

		choice = input("Choose an option: ").strip()

		if choice == "1":
			view_feed()
		elif choice == "2":
			add_post()
		elif choice == "3":
			like_post()
		elif choice == "4":
			delete_post()
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Please choose an option from 1 to 5.\n")


if __name__ == "__main__":
	main()
