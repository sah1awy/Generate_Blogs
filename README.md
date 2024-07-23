# Generate Blogs  

- The blog generator app utilizes the LLAMA 2 large language model, an open-source model created by Meta.
- The LLaMA model is indeed built upon the transformer architecture.
  

## Transformer Architecture  

  

**Encoder**: Processes the input sequence and generates a representation of it.
- Self-attention: Allows the model to weigh the importance of different parts of the input sequence in relation to each other.
- Feed-forward neural network: Applies non-linear transformations to the output of self-attention.

  
**Decoder**: Generates the output sequence based on the encoder's output.
- Self-attention: Similar to the encoder, but also attends to previously generated output tokens.
- Encoder-decoder attention: Allows the decoder to focus on relevant parts of the encoded input.
- Feed-forward neural network: Applies non-linear transformations.


## Steps
- Downloaded the Llama-2-7b-chat.ggmlv3.q6 model from Hugging Face.
- Installed necessary libraries and dependencies specified in requirements.txt.
- Created a Streamlit app to gather user input for blog topic, style, and number of words.
- Implemented a getLLama function to process inputs and generate text using the Llama model.
- Displayed the generated text using Streamlit.write().
