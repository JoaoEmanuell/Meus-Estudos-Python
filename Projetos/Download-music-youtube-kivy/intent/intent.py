class Intent:
    # https://github.com/olivier-boesch/intent-demo-for-kivy/tree/c2c36a70d3ca15c792d7b8a1811a3482ba6fe6b1
    def __init__(self, platform : str) -> None:
        self.platform = platform
        if self.platform == 'android' :
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            activity = PythonActivity.mActivity
            intent = activity.getIntent() # Intent
            self.intent_text = str(intent.getStringExtra(Intent.EXTRA_TEXT)) # Get the text
            self.intent_type = str(intent.getType()) # Get the type

    def get_intent_text(self) -> str:
        if self.platform == 'android' :
            if self.intent_text is not None and self.intent_type == 'text/plain':
                return self.intent_text
            else : return ''
        else : return ''