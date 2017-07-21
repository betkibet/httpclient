import requests


def info(url, uid):
	try:
		isinstance(int(uid), int)
		if int(uid) <= 20 and int(uid) > 0:
			data = requests.get(url + uid)
			return data
		else:
			print("Only integers are allowed between 1 and 20")
	except ValueError as e:
		print("No fractions or decimals allowed")
		raise(e)
	return "Empty information"

def post_data(url, title, content, user=11):
	article = {
		'title': title,
		'content': content,
		'user': user
		}
	data = requests.post(url, data=article)
	return data

def main():
	print("\n\t*** HTTP Client API Commandline Application ***\n\t%s\n" %("-"*31))
	print("Welcome user. This is a simple HTTP API client that lets you post an article")
	print("Fetch JSON code")
	urlcode = "https://jsonplaceholder.typicode.com/posts/"

	uid = input("Type an integer between 1 and 20 ")
	print("\n\tProcessing your data\n")
	fetch_data = get_data(urlcode,uid)
	print("\tGET Response data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,fetch_data.text, "-"*11, fetch_data.status_code,"-"*7, fetch_data.headers))

	print("\nCreate an article with a title and a content section")
	title = input("Create a title for your article")
	content = input("Create the contents section ")

	print("\n\tCreating your new post...\n")
	store_data = post_data(urlcode,title,content)
	print("\tPOST data\n\t%s\n%s\n\tStatus code\n\t%s\n%s\n\tHeaders\n\t%s\n%s" % 
		("-"*17,store_data.text, "-"*11, store_data.status_code,"-"*7, store_data.headers))

if __name__ == '__main__':
	main()
