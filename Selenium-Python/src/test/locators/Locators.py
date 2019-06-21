'''
Created on Jun 20, 2019

@author: saif.khan
'''
class Locators():
    # Login Screen Objects
    userid_text_name = "email"
    password_text_name = "password"
    login_submit_xpath="//button[@class='login_btn']"
    
    # Home Screen Objects
    ripple_menu_xpath = "//span[@class='ripple']"
    settings_link_xpath = "//i[@class='fa fa-cog fa-lg']"
    logout_link_xpath="// a[contains(text(), 'Log Out')]"

    vault_menu_xpath = "//a[contains(text(),'Vault')]"
    vault_subMenu_xpath="//a[contains(text(),'Stock Deposit/Withdraw')]"
    
    
    # Vault Screen Objects