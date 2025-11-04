import gradio as gr
from frontend.input_handlers import InputHandlers
from config import Config

# List of reference images (file paths in the Space)
reference_images = [
    "reference_images/35556692.jpg",
    "reference_images/35556705.jpg",
    "reference_images/35556710.jpg",
    "reference_images/35556713.jpg",
    "reference_images/35556714.jpg",
    "reference_images/35556760.jpg",
]

def create_gradio_interface():
    with gr.Blocks(title="Jewelry Recommender") as demo:
        gr.Markdown("# Jewelry Recommendation System by Maaz.dev💻")
        gr.Markdown("Upload an image or select a reference image to get recommendations.")
        
        # Define shared components first so they can be used in all tabs
        num_recs_slider = gr.Slider(
            minimum=1, 
            maximum=20, 
            value=5, 
            step=1, 
            label="Number of Recommendations"
        )
        skip_exact = gr.Checkbox(
            value=True, 
            label="Skip Exact Match"
        )

        with gr.Tab("Reference Images"):
            gr.Markdown("### Select a reference image to test:")
            
            # Gallery with images set to 300x300 display size
            reference_gallery = gr.Gallery(
                value=reference_images,
                columns=3,
                object_fit="cover",  # 'cover' will ensure the image fills the specified dimensions
                height="300px",     # Set gallery image height
                label="Click on an image to select"
            )
            
            # Store the selected image path
            selected_image_path = gr.State(value=reference_images[0])
            
            # Display the currently selected image at 300x300
            selected_display = gr.Image(
                value=reference_images[0],
                label="Selected Reference Image",
                height=300,
                width=300
            )
            
            gallery_output = gr.HTML(label="Recommendations")
            
            # Function to handle image selection from gallery
            def select_reference_image(evt: gr.SelectData, gallery_images):
                selected_path = reference_images[evt.index]  # Get the actual file path
                return selected_path, selected_path
            
            # Connect gallery selection to update the selected image
            reference_gallery.select(
                select_reference_image,
                inputs=[reference_gallery],
                outputs=[selected_image_path, selected_display]
            )
            
            # Add a button to get recommendations for the selected image
            ref_submit_btn = gr.Button("Get Recommendations for Selected Image")
            
            # Processing reference image
            ref_submit_btn.click(
                InputHandlers.process_image, 
                inputs=[selected_image_path, num_recs_slider, skip_exact], 
                outputs=gallery_output
            )
        
        with gr.Tab("Upload Image"):
            # Upload image component with 300x300 display size
            image_input = gr.Image(
                type="pil", 
                label="Upload Jewelry Image",
                height=300,
                width=300
            )
            submit_btn = gr.Button("Get Recommendations")
            output_html = gr.HTML(label="Recommendations")
            
            # Processing uploaded image
            submit_btn.click(
                InputHandlers.process_image, 
                inputs=[image_input, num_recs_slider, skip_exact], 
                outputs=output_html
            )
            
        with gr.Tab("Image URL"):
            url_input = gr.Textbox(label="Enter Image URL")
            
            # Preview of the URL image at 300x300
            url_preview = gr.Image(
                label="Image Preview",
                height=300,
                width=300,
                visible=False
            )
            
            # Function to update the preview when URL is entered
            def update_preview(url):
                return gr.update(value=url, visible=True)
            
            # Button to preview the URL image
            preview_btn = gr.Button("Preview Image")
            preview_btn.click(
                update_preview,
                inputs=[url_input],
                outputs=[url_preview]
            )
            
            url_btn = gr.Button("Get Recommendations from URL")
            url_output = gr.HTML(label="Recommendations")
            
            # Processing URL image
            url_btn.click(
                InputHandlers.process_url, 
                inputs=[url_input, num_recs_slider, skip_exact], 
                outputs=url_output
            )
            
        gr.Markdown("## How to Use")
        gr.Markdown("""
        1. Upload an image of jewelry, provide an image URL, or select a reference image from the gallery.
        2. Adjust the number of recommendations.
        3. Click 'Get Recommendations' to see similar jewelry items.
        """)
        
        return demo
# import gradio as gr
# from frontend.input_handlers import InputHandlers
# from config import Config

# # List of reference images (file paths in the Space)
# reference_images = [
#     "reference_images/35556692.jpg",
#     "reference_images/35556705.jpg",
#     "reference_images/35556710.jpg",
#     "reference_images/35556713.jpg",
#     "reference_images/35556714.jpg",
#     "reference_images/35556760.jpg",
# ]

# def create_gradio_interface():
#     with gr.Blocks(title="Jewelry Recommender") as demo:
#         gr.Markdown("# Jewelry Recommendation System")
#         gr.Markdown("Upload an image or select a reference image to get recommendations.")
        
#         # Define shared components first so they can be used in all tabs
#         num_recs_slider = gr.Slider(
#             minimum=1, 
#             maximum=20, 
#             value=5, 
#             step=1, 
#             label="Number of Recommendations"
#         )
#         skip_exact = gr.Checkbox(
#             value=True, 
#             label="Skip Exact Match"
#         )

#         with gr.Tab("Reference Images"):
#             gr.Markdown("### Select a reference image to test:")
            
#             # Replace dropdown with an image gallery for reference selection
#             reference_gallery = gr.Gallery(
#                 value=reference_images,
#                 columns=3,
#                 object_fit="contain",
#                 height="auto",
#                 label="Click on an image to select"
#             )
            
#             # Store the selected image path (not the image itself)
#             selected_image_path = gr.State(value=reference_images[0])
            
#             # Display the currently selected image
#             selected_display = gr.Image(
#                 value=reference_images[0],
#                 label="Selected Reference Image",
#                 height=200
#             )
            
#             gallery_output = gr.HTML(label="Recommendations")
            
#             # Function to handle image selection from gallery
#             def select_reference_image(evt: gr.SelectData, gallery_images):
#                 selected_path = reference_images[evt.index]  # Get the actual file path
#                 return selected_path, selected_path
            
#             # Connect gallery selection to update the selected image
#             reference_gallery.select(
#                 select_reference_image,
#                 inputs=[reference_gallery],
#                 outputs=[selected_image_path, selected_display]
#             )
            
#             # Add a button to get recommendations for the selected image
#             ref_submit_btn = gr.Button("Get Recommendations for Selected Image")
            
#             # Processing reference image - make sure we're passing the file path, not the image object
#             ref_submit_btn.click(
#                 InputHandlers.process_image, 
#                 inputs=[selected_image_path, num_recs_slider, skip_exact], 
#                 outputs=gallery_output
#             )
        
#         with gr.Tab("Upload Image"):
#             image_input = gr.Image(type="pil", label="Upload Jewelry Image")
#             submit_btn = gr.Button("Get Recommendations")
#             output_html = gr.HTML(label="Recommendations")
            
#             # Processing uploaded image
#             submit_btn.click(
#                 InputHandlers.process_image, 
#                 inputs=[image_input, num_recs_slider, skip_exact], 
#                 outputs=output_html
#             )
            
#         with gr.Tab("Image URL"):
#             url_input = gr.Textbox(label="Enter Image URL")
#             url_btn = gr.Button("Get Recommendations from URL")
#             url_output = gr.HTML(label="Recommendations")
            
#             # Processing URL image
#             url_btn.click(
#                 InputHandlers.process_url, 
#                 inputs=[url_input, num_recs_slider, skip_exact], 
#                 outputs=url_output
#             )
            
#         gr.Markdown("## How to Use")
#         gr.Markdown("""
#         1. Upload an image of jewelry, provide an image URL, or select a reference image from the gallery.
#         2. Adjust the number of recommendations.
#         3. Click 'Get Recommendations' to see similar jewelry items.
#         """)
            
#         return demo