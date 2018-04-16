class UsersPage

  #CSS Selectors
  BANNER = {id: "flash_success"}
  attr_reader :driver

  def initialize(driver)
    @driver = driver
  end

  #Class Methods
  def get_banner_text()
    banner = @driver.find_element(BANNER)
    banner.text
  end
  
end
