#Loader not working for now
#from langchain.document_loaders import YoutubeLoader
from langchain.document_loaders import UnstructuredHTMLLoader

#from langchain.llms import OpenAi

#loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True)

loader = UnstructuredHTMLLoader("https://vegan.com/info/why/")
result = loader.load()

print(result)