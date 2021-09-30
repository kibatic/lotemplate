import unittest
import ootemplate as ot
import test_json_convertion

cnx = ot.Connexion("localhost", "2002")


def to_data_list(file: str) -> list:
    return [ot.convert_to_datas_template(file, test_json_convertion.file_to_dict(file)), file]


class Text(unittest.TestCase):

    temp = ot.Template("files/comparaison/text_vars.odt", cnx, True)

    def test_valid(self):
        self.temp.search_error(*to_data_list("files/comparaison/text_vars_valid.json"))

    def test_invalid_supplement_variable(self):
        with self.assertRaises(ot.err.JsonUnknownVariable):
            self.temp.search_error(*to_data_list("files/comparaison/text_vars_invalid_variable.json"))

    def test_invalid_missing_variable(self):
        with self.assertRaises(ot.err.JsonMissingRequiredVariable):
            self.temp.search_error(*to_data_list("files/comparaison/text_vars_invalid_missing_variable.json"))

    def test_invalid_incorrect_value(self):
        with self.assertRaises(ot.err.JsonIncorrectValueType):
            self.temp.search_error(*to_data_list("files/comparaison/text_vars_incorrect_value.json"))

    temp_tab = ot.Template("files/comparaison/static_tab.odt", cnx, True)

    def test_tab_valid(self):
        self.temp_tab.search_error(*to_data_list("files/comparaison/static_tab_valid.json"))


class Tables(unittest.TestCase):

    temp = ot.Template("files/comparaison/two_row_tab_varied.odt", cnx, True)

    def test_valid(self):
        self.temp.search_error(*to_data_list("files/comparaison/two_row_tab_varied_valid.json"))

    def test_invalid_missing_variable(self):
        with self.assertRaises(ot.err.JsonMissingRequiredVariable):
            self.temp.search_error(
                *to_data_list("files/comparaison/two_row_tab_varied_invalid_missing_argument_all_rows.json")
            )

    def test_invalid_unknown_variable(self):
        with self.assertRaises(ot.err.JsonUnknownVariable):
            self.temp.search_error(*to_data_list("files/comparaison/two_row_tab_varied_invalid_unknown_argument.json"))


class Images(unittest.TestCase):

    temp = ot.Template("files/comparaison/img_vars.odt", cnx, True)

    def test_valid(self):
        self.temp.search_error(*to_data_list("files/comparaison/img_vars_valid.json"))

    def test_invalid_unknown_variable(self):
        with self.assertRaises(ot.err.JsonUnknownVariable):
            self.temp.search_error(*to_data_list("files/comparaison/img_vars_invalid_other_image.json"))


if __name__ == '__main__':
    unittest.main()
