from pytube import YouTube
link=input("Paste your link here : ")
y1=YouTube(link)
print(y1.title)
print(y1.thumbnail_url)
videos=y1.streams.all()
vids=list(enumerate(videos))
for i in vids:
    print(i)
print("Processing please wait !!!")
strm=int(input("Enter Stream No = "))
videos[strm].download()
print("Successfully Downloaded in your program file location...!")