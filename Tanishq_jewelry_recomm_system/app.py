# main.py
from frontend.gradio_app import create_gradio_interface

def main():
    """Main entry point to run the Jewelry Recommender application."""
    print("Starting Jewelry Recommender System...")
    demo = create_gradio_interface()
    demo.launch()

if __name__ == "__main__":
    main()
