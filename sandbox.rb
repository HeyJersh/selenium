require "selenium-webdriver"
require "rspec"
require_relative "SignupPage.rb"
require_relative "UsersPage.rb"

timestamp = Time.now.to_i
username = "user#{timestamp}"
email = "user#{timestamp}@test.com"
password = "password"
expected_banner_text = "Welcome to the alpha blog user#{timestamp}"

#TEST 0:  Sign Up for Blog
describe "Blog" do
  describe "Sign Up" do
    it "should confirm a user can successfully signed up" do
      #0.1: Go to signup form
      @driver = Selenium::WebDriver.for :remote, desired_capabilities: :firefox
      @driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

      #0.2: Fill out the form
      signup = SignupPage.new(@driver)
      signup.enter_username(username)
      signup.enter_email(email)
      signup.enter_pass(password)
      signup.submit_form()

      #0.3 Confirm user signed up successfully
      users = UsersPage.new(@driver)
      banner_text = users.get_banner_text()
      expect(banner_text).to eq(expected_banner_text)

      @driver.quit
    end
  end
end
