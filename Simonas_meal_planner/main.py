from dotenv import load_dotenv

def main():
    load_dotenv()  # Load environment variables from .env file

    from controllers.main_controller import MainController

    main_controller = MainController()
    main_controller.run()

if __name__ == "__main__":
    main()
