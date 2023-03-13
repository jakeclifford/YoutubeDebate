from langchain.agents import load_tools
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

tool_names = ["wikipedia"]
tools = load_tools(tool_names)

wiki = tools[0]("james cook")

print(llm("Can you sumarise {wiki}"))