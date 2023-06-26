from django.test import SimpleTestCase, Client


class UrlTest(SimpleTestCase):
    def test_true_is_true(self):
        self.assertEqual(1, 1)

    def test_get_observations(self):
        paths = {
            "index": "/",
            "observations-municipalite": "report/ou/7/",
        }
        for name, _path in paths.items():
            response = self.client.get(_path)
            self.assertAlmostEqual(200, response.status_code, f"{name} {_path} paths failed")
