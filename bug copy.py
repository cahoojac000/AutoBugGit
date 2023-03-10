from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password = "Yoohoo6902!*"

class bug:
  driver = None
  wait = None
  def setup(self):
    self.driver = webdriver.Chrome()
    #options = webdriver.ChromeOptions()
    #options.add_experimental_option("debuggerAddress", "localhost:9222")
    #self.driver = webdriver.Chrome(options=options)
    self.wait = WebDriverWait(self.driver, 10)
    #self.driver.execute_script("window.open('', '_blank');")

  def autoinput(self, id, input):
    self.wait.until(EC.presence_of_element_located((By.NAME, id)))
    field = self.driver.find_element(By.NAME, id)
    field.clear()
    field.send_keys(input)
  
  def autoclick(self, xpath):
    self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    self.driver.find_element(By.XPATH, xpath).click()

  def login(self):
    self.driver.find_element(By.ID, "login").send_keys("meganvee")
    self.driver.find_element(By.ID, "password").send_keys(password)
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

  def run(self):
    xpaths = ["/html/body/table/tbody/tr[1]/td/div[2]/ul/li[2]/a", "/html/body/table/tbody/tr[2]/td/div[2]/div/div[1]/form/div[2]/table[1]/tbody/tr[10]/td/div/table/tbody/tr[7]/td[3]/div/a[1]", "/html/body/table/tbody/tr[2]/td/div[2]/div[1]", "/html/body/table/tbody/tr[2]/td/div[2]/div[2]/fieldset/ul/li[1]/a"]

    self.driver.get("https://scan-bugs.org/portal/profile/index.php?refurl=/portal/index.php?")

    self.wait.until(EC.presence_of_element_located((By.ID, "login")))

    self.login()

    for xpath in xpaths:
      self.autoclick(xpath)
  
  def autofill(self, tokens):
    ids = ["catalognumber", "recordedby", "eventdate", "sciname", "dateidentified", "associatedtaxa", "sex", "individualcount", "fieldnumber", "scientificnameauthorship"]
    for id, token in zip(ids, tokens):
      self.autoinput(id, token)
    #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")