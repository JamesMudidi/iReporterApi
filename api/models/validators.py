class Validator:
    """
    validate the various inputs before  passing them to the list
    """

    def pure_test(self,text):
        if self.normal_string(text):
            if text.strip().isalpha() == True:
                return text

    def normal_string(self,text):
        if isinstance(text, str):
            new_text = str(text).strip
            if not new_text:
                return 
            return new_text
        else:
            return


    def order_id(self, number):
        if isinstance(number, int):
            if number > 0:
                return number

            else:
                return
        else:
            return
