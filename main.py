import argparse
from openrgb import OpenRGBClient
from effects import EffectsManager

def list_effects(effects_manager):
    """List all available effects."""
    print("Available Effects:")
    for idx, effect_name in enumerate(effects_manager.get_effects_list(), start=1):
        print(f"{idx}. {effect_name}")

def main():
    # Connect to OpenRGB
    try:
        client = OpenRGBClient()
    except Exception as e:
        print(f"Error connecting to OpenRGB: {e}")
        return

    # Load effects
    effects_manager = EffectsManager(client)

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Control RGB lighting effects.")
    parser.add_argument(
        "--list", action="store_true", help="List all available effects."
    )
    parser.add_argument(
        "--run", type=str, help="Run a specific effect by its name."
    )

    args = parser.parse_args()

    if args.list:
        list_effects(effects_manager)
        return

    if args.run:
        effect_name = args.run
        if effect_name in effects_manager.get_effects_list():
            print(f"Running effect: {effect_name}")
            effects_manager.run_effect(effect_name)
        else:
            print(f"Effect '{effect_name}' not found.")
        return

    # Interactive mode if no arguments provided
    print("Welcome to RGB Effects CLI!")
    list_effects(effects_manager)

    while True:
        try:
            choice = input(
                "\nEnter the effect name to run (or type 'exit' to quit): "
            ).strip()

            if choice.lower() == "exit":
                print("Exiting...")
                break

            if choice in effects_manager.get_effects_list():
                print(f"Running effect: {choice}")
                effects_manager.run_effect(choice)
            else:
                print(f"Effect '{choice}' not found. Try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
