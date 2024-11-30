import os
import importlib

class EffectsManager:
    def __init__(self, client):
        self.client = client
        self.effects = self.load_effects()

    def load_effects(self):
        """Dynamically load all effect modules from the Effects directory."""
        effects_dir = os.path.join(os.path.dirname(__file__), "Effects")
        effects = {}

        for filename in os.listdir(effects_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                effect_name = filename[:-3]  # Strip .py extension
                module_name = f"Effects.{effect_name}"
                try:
                    module = importlib.import_module(module_name)
                    class_name = getattr(module, effect_name)  # Class name matches file name
                    effects[effect_name] = class_name(self.client)
                except Exception as e:
                    print(f"Error loading effect {effect_name}: {e}")
        
        return effects

    def get_effects_list(self):
        """Get a list of available effects."""
        return list(self.effects.keys())

    def run_effect(self, effect_name):
        """Run the specified effect."""
        if effect_name in self.effects:
            effect = self.effects[effect_name]
            try:
                effect.start_effect()
            except Exception as e:
                print(f"Error running effect {effect_name}: {e}")
        else:
            print(f"Effect {effect_name} not found.")
