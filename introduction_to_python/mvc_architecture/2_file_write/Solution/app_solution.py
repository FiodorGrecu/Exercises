import view_solution as view
import model_solution as model

file_name = input(view.ask_fileName())
model.create(file_name)

content = input(view.ask_content())
model.write(content, file_name)
data = model.read(file_name)

result = view.display(data)
print(result)


