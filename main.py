import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import undetected_chromedriver as uc
class PokemonSearch(unittest.TestCase):
    def setUp(self):
        self.driver = uc.Chrome()
    def test_search_pikachu(self):
        driver = self.driver     
        driver.get("https://www.pokemon.com/us")
        driver.maximize_window()
        self.assertIn("Pokémon", driver.title)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@class=\"title title_pokeball\" and text()=\"Pokédex\"]"))

        )
        driver.find_element(By.XPATH, "//*[@class=\"title title_pokeball\" and text()=\"Pokédex\"]").click()
        self.assertIn("Pokédex", driver.title)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        driver.find_element(By.ID, "searchInput").send_keys("Pikachu")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        driver.find_element(By.ID, "search").click()

        element =  WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//figure/a[@href=\"/us/pokedex/pikachu\"]/img"))
        )
        driver.find_element(By.XPATH, "//figure/a[@href=\"/us/pokedex/pikachu\"]/img").click()
        self.assertIn("Pikachu", driver.title)

        element = driver.find_element(By.XPATH, "//a[@href=\"/us/pokedex/\" and @class=\"button button-orange right\"]")
        total_height = int(driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, int(total_height/2.5), 5):
            driver.execute_script("window.scrollTo(0, {});".format(i))
            

        element.click()
        self.assertIn("Pokédex", driver.title)

        total_height = int(driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 5):
            driver.execute_script("window.scrollTo(0, {});".format(i))
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()