from bs4 import BeautifulSoup
import re

from walkoff_app_sdk.app_base import AppBase

class Cleaner(AppBase):
    __version__ = "0.0.1"
    app_name = "Text_Clean"  

    def __init__(self, redis, logger, console_logger=None):
        print("INIT")
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    # This is dangerously fun :)
    # Do we care about arbitrary code execution here?
    # Probably not huh

    def clean_html(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.decompose()
        
        cleaned_text = re.sub(r'\s+', ' ', soup.get_text())
        
        cleaned_text = cleaned_text.strip().replace('\\r', '').replace('\\n', '')
        
        return cleaned_text



if __name__ == "__main__":
    Cleaner.run()