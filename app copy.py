import gradio as gr
from bug.bug import bug

driver = bug()

def login():
   driver.setup()
   return driver.run()

def autofillsubmit(text):
   tokens = str(text).split('\n')
   author = tokens.pop(5)
   tokens.append(author)
   return driver.autofill(tokens)

def main():   
   with gr.Blocks() as interface:
      loginButton = gr.Button(value="Login")
      loginButton.click(login, inputs=None, outputs=None)

      with gr.Row():
         gr.Textbox(placeholder="Catalog Number\nCollector\nDate\nScientific Name\nDate Identified\nAuthor\nAssociated Taxa\nSex\nIndividual Count\nField Number", interactive=False, label="Input Structure:")
         text = gr.Textbox(label="Enter the data here, love :)")
      inputButton = gr.Button(value="Autofill")
      inputButton.click(autofillsubmit, inputs=text, outputs=None)
      interface.launch(inbrowser=True)