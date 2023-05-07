def make_album(artist_name="", artist_title="", no_of_tracks=""):
	"Return the Dictionary"
	artist_details = {"artist_name": artist_name,"artist_title": artist_title}
	if no_of_tracks:
		artist_details['no_of_tracks'] = no_of_tracks
	return artist_details

while True:
	print("Enter the Artist Details")
	print(("Enter Q at any time to exit"))

	artist_name = input("Enter the Artist Name:")
	if artist_name == 'q':
		break

	artist_title = input("Enter the Artist Title:")
	if artist_title == 'q':
		break

	no_of_tracks = input("Enter the number of tracks if known:")
	if no_of_tracks:
		artist_details = make_album(artist_name, artist_title,no_of_tracks)
	else:
	 	artist_details = make_album(artist_name, artist_title)

	print(artist_details)

