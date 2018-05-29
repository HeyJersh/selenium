class SignupPage
  #CSS Selectors
  USERNAME_FIELD = {id: "user_username"}
  USEREMAIL_FIELD = {id: "user_email"}
  USERPASS_FIELD = {id: "user_password"}
  SUBMIT_BUTTON = {id: "submit"}

  attr_reader :driver

  #class methods
  def initialize(driver)
    @driver = driver
  end

  def enter_username(username)
    username_field = @driver.find_element(USERNAME_FIELD)
    username_field.send_keys(username)
  end

  def enter_email(email)
    useremail_field = @driver.find_element(USEREMAIL_FIELD)
    useremail_field.send_keys(email)
  end

  def enter_pass(password)
    pass_field = @driver.find_element(USERPASS_FIELD)
    pass_field.send_keys(password)
  end

  def submit_form()
    submit_button = @driver.find_element(SUBMIT_BUTTON)
    submit_button.click
  end


end
