import pytube
url=input("enter video url: ")
path=""  #path içi boş kalırsa python projelerinin kaydedildiği yere kaydeder. veya yolu kendin verirsin. pycharm projects-> yt downloads python kutuphanelerini arastır
pytube.YouTube(url).streams.get_highest_resolution().download(path)
