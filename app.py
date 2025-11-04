import pandas as pd
import gradio as gr


# Load dataset
df = pd.read_csv("tjd_sorted_file.csv")

# Simple jewelry recommender function
def recommend_jewelry(item_name):
    # Filter dataset by matching name
    results = df[df['item_name'].str.contains(item_name, case=False, na=False)]
    if results.empty:
        return "No similar jewelry found."
    return results.head(5)

# Create Gradio interface
demo = gr.Interface(
    fn=recommend_jewelry,
    inputs=gr.Textbox(label="Enter Jewelry Name"),
    outputs="dataframe",
    title="Tanishq Jewelry Recommendation System",
    description="Search and discover similar jewelry items from the Tanishq dataset."
)

# Launch app
demo.launch()
