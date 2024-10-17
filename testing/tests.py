from textual_englyph import EnGlyph
from textual.app import App, ComposeResult

class Test(App):

    def compose(self) -> ComposeResult:
        yield EnGlyph("Hello!")

if __name__ == "__main__":
    Test().run()
